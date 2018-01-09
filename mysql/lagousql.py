# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: lagousql.py

@time: 2018/1/8 22:15

@desc:

'''
import pymysql
count = 0
conn = pymysql.connect(host='127.0.0.1', user='root', password='213', db='lagou', charset="utf8")

cur = conn.cursor()

sqlc = '''
               create table lagous(
               id int(11) not null auto_increment primary key,
               gongsi varchar(255) not null,
               zhiwei varchar(255),
               gongzi varchar(255),
               tedian varchar(255),
               logo varchar(255),
               gongsijieshao varchar(255),
               xiangxiwangzhi varchar(255),
               rukushijian datetime )DEFAULT CHARSET=utf8;
               '''

try:
    A = cur.execute(sqlc)
    conn.commit()
    print('成功')
except:
    print("错误")

sqla = '''
        insert into  lagous(gongsi,zhiwei)
        values(%s,%s);
       '''
try:
    B = cur.execute(sqla, ("ming", "HOHO"))
    conn.commit()
    print('成功')
except:
    print("错误")
