# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: trymysql.py

@time: 2018/1/8 18:51

@desc:

'''

import requests
import re
import pymysql


def getHTMLtext(url):
    try:
       r=requests.get(url,timeout=100)
       r.raise_for_status()
       r.encoding=r.apparent_encoding

       return r.text
    except:
        return ""
def getpage(itl,html):
    try:
        plt=re.findall(r'"view_price":"[\d.]*"',html)
        nlt=re.findall(r'"raw_title":".*?"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(nlt[i].split(':')[1])
            itl.append([price, title])
    except:
       print("")


def printgoods(itl):
    tplt = "{:2}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))

    count = 0
    conn = pymysql.connect(host='127.0.0.1', user='root', password='213', db='lagou',charset="utf8")

    cur = conn.cursor()

    sqlc = '''
                create table coffee1(
                id int(11) not null auto_increment primary key,
                name varchar(255) not null,
                price float not null)DEFAULT CHARSET=utf8;
                '''

    try:
        A = cur.execute(sqlc)
        conn.commit()
        print('成功')
    except:
        print("错误")
    for g in itl:
        count = count + 1
        b=tplt.format(count, g[0], g[1])



        sqla = '''
        insert into  coffee1(name,price)
        values(%s,%s);
       '''
        try:
            B = cur.execute(sqla,(g[1],g[0]))
            conn.commit()
            print('成功')
        except:
            print("错误")

        # save_path = 'D:/taobao.txt'
        # f=open(save_path,'a')
        #
        # f.write(b+'\n')
        # f.close()

    conn.commit()
    cur.close()
    conn.close()


def main():
    goods="咖啡"
    depth =2
    start_url='https://s.taobao.com/search?q='+goods
    List =[]
    for i in range(depth):
        try:
            url =start_url +"&s="+ str(i*44)
            html=getHTMLtext(url)

            getpage(List,html)
        except:
           continue


    print(printgoods(List))
    # savefiles(data)




main()