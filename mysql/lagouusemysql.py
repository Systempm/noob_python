# encoding: utf-8

'''

@author: caopeng

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com

@software: garner

@file: lagou.py

@time: 2017/12/23 14:53

@desc:

'''
import time

import datetime
import pymysql
import requests
from bs4 import BeautifulSoup


class message_url:
    global pzdata
    def message_body(self,url,headers):
        response=requests.post(url,headers=headers)
        response.close()#11
        print( type(response))
        m=response.text
        return m

    def split_slary(self, salary):

        lowsalary, highsalary = salary.split("-")
        lenlow=len(lowsalary)
        lenhigh = len(highsalary)
        lowsalary=lowsalary[:lenlow-1]
        highsalary = highsalary[:lenhigh - 1]
        return lowsalary,highsalary
    # 此处配置文件位置 ！！！！！！# 此处配置文件位置 ！！！！！！
    # 此处配置文件位置 ！！！！！！# 此处配置文件位置 ！！！！！！
    # 此处配置文件位置 ！！！！！！# 此处配置文件位置 ！！！！！！
    def writedb(self,conn,list):
        global pzdata
        print (list)
        cur = conn.cursor()
        sqlc = '''
                       create table {tablename}(
                       id int(11) not null auto_increment primary key,
                       gongsi varchar(255) not null,
                       zhiwei varchar(255),
                       gongzi varchar(255),
                       minslary int(11),
                       maxslary int(11),
                       didian varchar(255),
                       tedian varchar(255),
                       logo varchar(255),
                       gongsijieshao varchar(255),
                       xiangxiwangzhi varchar(255),
                       rukushijian datetime 
                       )DEFAULT CHARSET=utf8;
                       '''.format(tablename=pzdata['tablename'])

        try:
            A = cur.execute(sqlc)
            conn.commit()
            print('成功')
        except:
            print("错误")

        sqla = '''
                insert into  {tablename}(gongsi,zhiwei,gongzi,minslary,maxslary,didian,tedian,logo,gongsijieshao,xiangxiwangzhi,rukushijian)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
               '''.format(tablename=pzdata['tablename'])
        try:
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            B = cur.execute(sqla, (list[0], list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9], dt))
            conn.commit()
            print('成功')
        except:
            print("错误")

    def file_openpz(self,url='D:\\pyProject\\toexcl\\mysql\\new.xml'):                     # 此处配置文件位置 ！！！！！！
        aaa=""
        print (url)
        fopen = open(url, 'r')
        for eachLine in fopen:
            aaa= aaa+eachLine
        fopen.close()
        aaa=eval(aaa)
        print (aaa)
        return aaa

    def start_craw(self,headers,url="https://www.lagou.com/{locals}-zhaopin/{page}/?filterOption={page}",local="shenyang",pagenum=5,conn="conn"):
        aaa = 0
        pagenum=int(pagenum)
        for page in range(1, pagenum):
            url =url.format(locals=local,page=page)
            a = message_url()
            # data={
            #     "first": 'true',
            #     "pn":  "1",
            #     "kd":  "python",
            #   }
            m = a.message_body(url, headers)
            print(type(m))
            soup = BeautifulSoup(m, "html.parser")  # 实例化一个BeautifulSoup对象
            soupp = soup(class_="con_list_item default_list")
            urlsoup = soup.find_all("a", {"class": "position_link"})
            locationsoup = soup.find_all("span", {"class": "add"})
            timesoup = soup.find_all("span", {"class": "format-time"})
            experience = soup.find_all("div", {"class": "p_bot"})  # 手动 拆分 薪水和 年限把11
            companyinformationsoup = soup.find_all("div", {"class": "company_name"})  # 里面有公司的网页 ！@#@#！@#￥
            companyspecial = soup.find_all("div", {"class": "industry"})
            logourlsoup = soup.find_all("div", {"class": "com_logo"})
            introductionsoup = soup.find_all("div", {"class": "li_b_r"})
            te = []

            for i in range(len(soupp)):
                companyname = soupp[i].attrs['data-company']
                salary = soupp[i].attrs['data-salary']
                positisioniame = soupp[i].attrs['data-positionname']
                location = locationsoup[i].text  # ????
                introduction = introductionsoup[i].text
                logourl = logourlsoup[i].img.attrs['src']
                companyinformation = companyinformationsoup[i].a.attrs['href']
                hrefurl = urlsoup[i].attrs['href']
                #切分 salary
                lowsalary,highsalary= ming.split_slary("ming",salary)
                list = [companyname, positisioniame, salary,int(lowsalary),int(highsalary), location, introduction, logourl, companyinformation,hrefurl]
                ming.writedb("ming",conn,list)

            print("一页完成")
            aaa = aaa + 1
            time.sleep(2)
            print(aaa)

if __name__ == '__main__':
    ming=message_url
    pzdata=ming.file_openpz("ming")  #先给我打开配置文件  #1()
    # 根据配置文件 连    接数据库！!
    conn = pymysql.connect(host='127.0.0.1', user='root', password='213', db='lagou', charset="utf8")
    # headers  的处理 还是要多多费心思 一下   可以选择  包括有cookies什么的
    #爬取数据部分
    # 头文件  解决！@#

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'Referer': 'http://bzclk.baidu.com/adrc.php?t=06KL00c00f7Ghk600n-u0FNkUsKbP14p00000c5j9db00000V_69gZ.THL0oUhY1x60UWdBmy-bIfK15yPWPHfznWFBnj0sPAuBPhn0IHdKPHF7fWTznjRznYPjwj9afbR1fHNKwHTYrHbsrDPKP0K95gTqFhdWpyfqn10Ln1RzPjRvnzusThqbpyfqnHm0uHdCIZwsrBtEILILQhk9uvqdQhPEUiqBuy-Jpy4MQgGCmyqspy3E5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAn0mLFW5Hnsn1nd&tpl=tpl_10085_15730_11224&l=1502069635&attach=location%3D%26linkName%3D%25E8%25A1%25A8%25E6%25A0%25BC2-2%26linkText%3D%25E5%258C%2597%25E4%25BA%25AC%26xp%3Did(%2522m23a441b3%2522)%252FDIV%255B1%255D%252FDIV%255B1%255D%252FDIV%255B3%255D%252FDIV%255B1%255D%252FTABLE%255B1%255D%252FTBODY%255B1%255D%252FTR%255B1%255D%252FTD%255B2%255D%252FA%255B1%255D%26linkType%3D%26checksum%3D12&ie=utf-8&f=8&tn=baidu&wd=%E6%8B%89%E5%8B%BE%E7%BD%91&oq=%25E7%2588%25AC%25E5%258F%2596%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%2520%25E9%259C%2580%25E8%25A6%2581%25E5%2593%25AA%25E4%25BA%259B%25E6%2595%25B0%25E6%258D%25AE&rqlang=cn&inputT=1316',
        'Origin': 'https://www.lagou.com'
               }
    ming.start_craw("ming",headers=headers,local=pzdata['local'],pagenum=pzdata['howmanypage'],conn=conn)
    # url1="https://www.lagou.com/beijing-zhaopin/?utm_source=m_cf_cpt_baidu_pc"