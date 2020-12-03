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

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        queryMess = """select username, passwd from TTDANGNHAPs where username='{}' and passwd='{}';""".format(username,password)
        cursor.execute(queryMess)
        data = cursor.fetchall()
        uname = str(data[0][0])
        passwd = str(data[0][1])
        if (request.form['username'] == uname and request.form['password'] == passwd):
            return redirect(url_for('index'))
        else:
            error = 'Thong tin dang nhap khong hop le! Hay thu lai.'
    conn.close()
    return render_template('login.html', error=error)
'''
#sql injection
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        queryMess = """select username, passwd from TTDANGNHAPs where username='{}' and passwd='{}';""".format(username,password)
        cursor.execute(queryMess)
        account = cursor.fetchall()
        if account:
            return redirect(url_for('index'))
        else:
            error = 'Thong tin dang nhap khong hop le! Hay thu lai.'
    conn.close()
    return render_template('login.html', error=error)
'''
@app.route('/display_user')
def get_users_info():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("select * from Users")
    data = cursor.fetchall()
    conn.close()
    return render_template('display_user.html', data=data)

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
        query = """select * from Users where hoten='{}';""".format(hoten)
        cursor.execute(query)
        conn.commit()
        data = cursor.fetchall()

        return render_template('display_user.html',data=data)
    conn.close()
    return render_template('search_user.html')

@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    error = None
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method =='POST':
        hoten = request.form['hoten']
        query = """select * from Users where hoten='{}';""".format(hoten)
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
    app.run(host='0.0.0.0', port=5000)
