
create table LoaiSPs
(
    loai_sp_masp varchar(255) not null
        primary key,
    xuatXu       varchar(255) null
);

create table SanPhams
(
    maSP         varchar(255) not null
        primary key,
    tenSP        varchar(255) null,
    dvt          varchar(255) null,
    gia          double       null,
    loai_sp_masp varchar(255) null,
    constraint SanPhams_ibfk_1
        foreign key (loai_sp_masp) references LoaiSPs (loai_sp_masp)
            on update cascade on delete set null
);

create index loai_sp_masp
    on SanPhams (loai_sp_masp);

create table Users
(
    maKH      varchar(255) not null
        primary key,
    hoten     varchar(255) null,
    dchi      varchar(255) null,
    sodt      varchar(255) null,
    ngSinh    datetime     null,
    ngDK      datetime     null,
    doanhSo    double       null
);

create table HoaDons
(
    HoaDonSoH       int          not null
        primary key,
    ngay        datetime     null,
    maKH      varchar(255) null,
    triGia       double       null,
    constraint HoaDons_ibfk_1
        foreign key (maKH) references Users (maKH)
            on update cascade on delete set null
);

create table CTHDs
(
    HoaDonSoH int          null,
    maSP      varchar(255) null,
    SL        int          null,
    constraint CTHDs_ibfk_1
        foreign key (HoaDonSoH) references HoaDons (HoaDonSoH)
            on update cascade on delete set null,
    constraint CTHDs_ibfk_2
        foreign key (maSP) references SanPhams (maSP)
            on update cascade on delete set null
);
create table TTDANGNHAPs (
    username varchar(20)  null,
    passwd varchar(20)  null,
    KHACHHANG_MAKH varchar(255)  null,
    constraint TTDANGNHAPs_ibfk_1
		foreign key(KHACHHANG_MAKH) references Users (maKH)
			on update cascade on delete set null
);

create index HoaDonSoH
    on CTHDs (HoaDonSoH);

create index maSP
    on CTHDs (maSP);

create index maKH
    on HoaDons (maKH);

insert into Users (maKH,hoten,dchi,sodt,ngSinh,ngDK,doanhSo)
values
    ('KH01','Nguyen Van A','731 Tran Hung Dao, Q5, TpHCM','8823451','1960-10-22','1980-10-2',13060000),
    ('KH02','Tran Van B','23/5 Nguyen Trai, Q5, TpHCM','908256478','1960-10-11','1980-10-2',280000),
    ('KH03','Nguyen Van C','45 Nguyen Canh Chan, Q1, TpHCM','938776266','1960-11-11','1980-10-2',3860000),
    ('KH04','Tran Minh Long','50/34 Le Dai Hanh, Q10, TpHCM','917325476','1968-10-5','1980-10-2',250000),
    ('KH05','Le Nhat Minh','34 Truong Dinh, Q3, TpHCM','8246108','1980-10-2','1982-10-6',21000);

insert into LoaiSPs (loai_sp_masp,xuatXu)
values
    ('BC','Singapore'),
    ('AC','Singapore'),
    ('TV','Trung Quoc'),
    ('SV','Trung Quoc'),
    ('ST','Viet Nam');

insert into SanPhams (maSP,tenSP,dvt,gia,loai_sp_masp)
values
    ('BC01','But chi 2B','cay',3000,'BC'),
    ('BC02','But chi 3B','cay',5000,'BC'),
    ('TV01','Tap 100 giay mong','quyen',2500,'TV'),
    ('TV02','Tap 200 giay mong','quyen',4500,'TV'),
    ('ST06','Phan viet bang','hop',5000,'ST'),
    ('ST07','Phan viet bang a','hop',7000,'ST');

insert into HoaDons (HoaDonSoH,ngay,maKH,triGia)
values
    (1001,'2006-10-5','KH01',320000),
    (1002,'2006-10-5','KH01',840000),
    (1003,'2006-10-5','KH02',100000),
    (1004,'2006-10-5','KH02',180000),
    (1005,'2006-10-5','KH03',3800000);

insert into CTHDs (HoaDonSoH,maSP,SL)
values
    (1001,'TV02',10),
    (1002,'TV01',5),
    (1003,'BC01',5),
    (1004,'BC02',10),
    (1005,'ST06',10);

insert into TTDANGNHAPs (username,passwd,KHACHHANG_MAKH)
values
	('nguyenvana','nguyenvana123','KH01'),
    ('tranvanb','tranvanb456','KH02'),
    ('nguyenvanc','nguyenvanc789','KH03');
   
select * from Users;
select * from LoaiSPs;
select * from SanPhams;
select * from CTHDs;
select * from HoaDons;
select * from TTDANGNHAPs;
/*--lay column name
SELECT COLUMN_NAME , ORDINAL_POSITION
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'test1' AND TABLE_NAME = 'Users';

select * from Users;
delete from Users where Users.hoten ='Tran Thi Van';

insert into Users (maKH,hoten,dchi,sodt,ngSinh,ngDK,doanhSo)
values('KH06','Tran Thi Van','123 Tran Hung Dao, Q5, TpHCM','889544','1970-10-22','1980-10-2',6060000);

select * from Users where hoten = 'Nguyen Van A';

update Users set hoten = 'Nguyen Van A', sodt = '456789'
where hoten = 'Nguyen Van B';

select username, passwd from TTDANGNHAPs where username='nguyenvana' and passwd='nguyenvana123';
*/

