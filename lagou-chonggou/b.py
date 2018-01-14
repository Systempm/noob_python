# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: b.py

@time: 2018/1/13 6:24

@desc:

'''
import pymysql
import json
import requests
import xlwt
import time
from lxml import etree
import random
from fake_useragent import UserAgent
import sys
# 获取 totalcount pn 返回 totalcount pn # 此处pn大于30 默认返回30  以后再做详细展开
def get_pn(url,cookies,headers,datas):
    # 'Referer': 'https://www.lagou.com/jobs/list_java?city=%E6%B2%88%E9%98%B3&cl=false&fromSearch=true&labelWords=&suginput=',
    content = requests.post(url=url,cookies=cookies,headers=headers,data=datas)
    time.sleep(15 + random.randint(0, 2))
    result = content.json()
    totalcount= result["content"]["positionResult"]["totalCount"]
    pagesize = result["content"]["pageSize"]
    pn =  totalcount/pagesize
    print(totalcount, pagesize, pn)
    if pn>30:
        pn =30
        return totalcount,pn
    return totalcount,pn

def get_json(url,cookies,headers,datas):
    # 'Referer': 'https://www.lagou.com/jobs/list_java?city=%E6%B2%88%E9%98%B3&cl=false&fromSearch=true&labelWords=&suginput=',

    print (datas)
    content = requests.post(url=url,cookies=cookies,headers=headers,data=datas)
    # content.encoding = 'utf-8'
    # resultstr= content.text
    time.sleep(15 + random.randint(0, 4))
    result = content.json()
    return result
#北京
# 'Referer':'https://www.lagou.com/jobs/list_Java?px=default&city=%E5%8C%97%E4%BA%AC',

def go_spider(list):
    print(list)
    #for 循环开始爬 抓数据：
    #失败的集合  pn
    faillist = []
    # for i in range(1, pn + 1):
    for i in list:
        datas1 = {'first': False, 'pn': '{pn}'.format(pn=i), 'kd': 'java' }
        resultset = get_json(url, cookies, headers, datas1)
        print (resultset["success"])
        print(resultset)
        # 判断success  是不是爬成功  ：
        return_result=resultset["success"]
        # if  return_result== True:
            #此处 过滤   录入到数据库

        #
        #
            # resultset = json.dumps(resultset, ensure_ascii=False)
            # filename = city + datas["kd"] + str(i) + ".txt"
            # with open(filename, "w") as f:
            #     f.write(resultset)
        if return_result == False:
            faillist.append(i)
            time.sleep(10)
    if len(faillist)!=0:
        go_spider(faillist)
def get_pnrangelist():
    # 先爬第一页 然后拿到pn的数量 还有total 的数  total 准备放到其他地方 也是一个重要数据
    totalcount, pn = get_pn(url, cookies, headers, datas)
    return range(1,pn+1)

def con_db():


    conn = pymysql.connect(host='127.0.0.1', user='root', password='213', db='lagou', charset="utf8")

    cur = conn.cursor()
    return conn ,cur
def db_createtable(conn,cur,tablename):
    sqlc = '''
                        create table {tablename}(
                        id int(11) not null auto_increment primary key,
                        companyShortName varchar(255) not null,
                        companyFullName varchar(255),
                        positionName varchar(255),
                        positionId varchar(255),
                        salary varchar(255),
                        minslary int(11),
                        maxslary int(11),
                        companyLogo varchar(255),
                        companySize varchar(255),
                        companyLabelList varchar(255),
                        city varchar(255),
                        district varchar(255),
                        businessZones varchar(255),
                        education varchar(255),
                        city varchar(255),
                       firstType varchar(255),
                        createTime datetime )DEFAULT CHARSET=utf8;
                        '''.format(tablename=tablename)

    try:
        A = cur.execute(sqlc)
        conn.commit()
        print('成功')
    except:
        print("错误")
def db_selectpositionId(conn,cur,positionId):

        sqla = '''
                    select * from lagou where positionId= %s;
                      '''
        try:
            B = cur.execute(sqla, positionId)
            conn.commit()
            print('成功',B)
        except:
            print("错误")


def db_select(conn, cur, id):
    sqla = '''
                    select * from lala where id= %s;
                      '''
    try:
        B = cur.execute(sqla, id)
        conn.commit()
        print(cur.fetchall())

        # rs = cursor.fetchone()
        print('成功', B)
    except:
        print("错误")


def process_data(list):

        print(type(list))
        list = json.loads(list)
        print (type(list))
        result=list["content"]["positionResult"]["result"]
        #  每一条 拿出来 positionId 看有没有  有更新时间 没有录入数据
        for i in result:
            positionId=i["positionId"]
            print (i["positionName"] )
if __name__ == '__main__':
    city = "北京"
    url = 'https://www.lagou.com/jobs/positionAjax.json?city={city}&needAddtionalResult=false&isSchoolJob=0'.format(
        city=city)
    # url='https://www.lagou.com/jobs/positionAjax.json?city=%E6%B2%88%E9%98%B3&needAddtionalResult=false&isSchoolJob=0'
    # url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false'
    datas = {'first': True, 'pn': 1, 'kd': 'java', }
    headers = {'Accept': 'application / json, text / javascript, * / *; q = 0.01', 'Connection': 'keep - alive',
               'charset': 'UTF - 8', 'Host': 'www.lagou.com', 'Origin': 'https: // www.lagou.com',
               'Referer': 'https://www.lagou.com/jobs/list_Java?px=default&city={city}',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'.format(
                   city=city)}
    cookies = {
        'Cookie': 'user_trace_token=20180112203339-3be4004e-a0d5-4156-bf0e-5c046af4e618; __guid=237742470.2605937090993304600.1515760413772.495; LGUID=20180112203340-d1cd8b7d-f794-11e7-a2ab-5254005c3644; JSESSIONID=ABAAABAAAGFABEF5FE7D1E04AAB29D57DA99D03DCDB9F33; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dg87l8AIIj_rluAiRfSyPdXc6ad0IbFL7YiS8PxTYJN3%26wd%3D%26eqid%3D88f80f4300015b55000000035a592d78; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=b45496bd79dcd7ed322dd73e5171e835; _gid=GA1.2.928823699.1515760415; _ga=GA1.2.50887905.1515760415; LGSID=20180113054948-82707980-f7e2-11e7-93d3-525400f775ce; LGRID=20180113060746-057201ab-f7e5-11e7-a2e1-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515760415,1515793781; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515794861; SEARCH_ID=baf015ec9ee84c419a20120f9fbc3bbc; monitor_count=38'}
    # info = get_json(url,datas,city)
    # datastt = {'first': True, 'pn': 40, 'kd': 'java', }
    # resultset = get_json(url, cookies, headers, datastt)
    # print (resultset)

    # aaa=""
    # fopen = open('D:\\pyProject\\toexcl\\lagou-chonggou\\北京1.13pm7\\北京java1.txt', 'r')
    # for eachLine in fopen:
    #     aaa = aaa + eachLine
    # fopen.close()
    # process_data(aaa)

    conn,cur=con_db()
    db_select(conn,cur,3)

    # pnlist= get_pnrangelist()
    # go_spider(pnlist)
