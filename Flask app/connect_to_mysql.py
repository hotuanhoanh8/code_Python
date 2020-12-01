from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL

app = Flask(__name__)
def get_db_connection():
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
    app.config['MYSQL_DATABASE_DB'] = 'test1'
    app.config['MYSQL_DATABASE_Host'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()
    return conn
"""
def get_info():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * from Users")
    data = cursor.fetchall()
    return data
"""
   
@app.route('/display')
def get_users_info():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * from Users")
    data = cursor.fetchall()
    conn.close()
    return render_template('display_table.html', data=data)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    error = None
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method =='POST':
        maKH = request.form['maKH']
        hoten = request.form['hoten']
        dchi = request.form['dchi']
        sodt = request.form['sodt']
        ngSinh = request.form['ngSinh']
        queryMess = """insert into Users (maKH,hoten,dchi,sodt,ngSinh,ngDK,doanhSo)
                        values('{}','{}','{}','{}','{}','1980-10-2',0);""".format(maKH,hoten,dchi,sodt,ngSinh)
        cursor.execute(queryMess)
        conn.commit()
        conn.close()
    return render_template('create_user.html', error=error)

@app.route('/get_user_info', methods=['GET', 'POST'])
def get_user_info():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method =='POST':
        hoten = request.form['hoten']
        query = """SELECT * from Users where hoten='{}';""".format(hoten)
        cursor.execute(query)
        conn.commit()
        data = cursor.fetchall()

        return render_template('display_table.html',data=data)
    conn.close()
    return render_template('search_user.html')

@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    error = None
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method =='POST':
        hoten = request.form['hoten']
        query = """SELECT * from Users where hoten='{}';""".format(hoten)
        cursor.execute(query)
        conn.commit()
        data = cursor.fetchall()

        return render_template('edit_user.html', data=data)
    if request.method =='POST':
        hoten = request.form['hoten']
        dchi = request.form['dchi']
        sodt = request.form['sodt']
        ngSinh = request.form['ngSinh']
        queryMess = """update Users set hoten='{}', dchi='{}', sodt='{}', ngSinh='{}' where hoten='{}';""".format(hoten,dchi,sodt,ngSinh,hoten)
        cursor.execute(queryMess)
        conn.commit()
        return render_template('edit_user.html')
    conn.close()
    return render_template('search_user.html', error=error)

@app.route('/delete_user', methods = ['GET','POST'])
def delete_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method =='POST':
        hoten = request.form['hoten']
        query = """delete from Users where hoten='{}';""".format(hoten)
        cursor.execute(query)
        conn.commit()
    conn.close()
    return render_template('delete_user.html')

    
if __name__ == "__main__":
    app.run(host='localhost', port=5000)
