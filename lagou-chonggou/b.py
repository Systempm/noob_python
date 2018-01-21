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
    time.sleep(3 + random.randint(0, 4))
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

        # print(resultset)
        # 判断success  是不是爬成功  ：
        return_result=resultset["success"]
        if  return_result== True:
        #此处 过滤   录入到数据库
               process_data(resultset)
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
def split_slary(salary):
        print (salary)
        try:
           lowsalary, highsalary = salary.split("-")
           lenlow=len(lowsalary)
           lenhigh = len(highsalary)
           lowsalary=lowsalary[:lenlow-1]
           highsalary = highsalary[:lenhigh - 1]
        # bug  会出现 “20k以上”这样的数据
        except:
            lowsalary=0
            highsalary=0
        return lowsalary,highsalary
def con_db():


    conn = pymysql.connect(host='127.0.0.1', user='root', password='213', db='lagou', charset="utf8")

    cur = conn.cursor()
    return conn ,cur
def db_createtable(conn,cur,tablename):
    sqlc = '''
                        create table {aaa}(
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
                        firstType varchar(255),
                        createTime datetime )DEFAULT CHARSET=utf8;
                        '''.format(aaa=tablename)
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
# def db_inserttable(conn,cur,resultlist):
#     companyShortName=resultlist["companyShortName"]
#     companyFullName=resultlist["companyFullName"]
#     positionName=resultlist["positionName"]
#     positionId=resultlist["positionId"]
#     salary=resultlist["salary"]
#     minslary=resultlist["minslary"]
#     maxslary=resultlist["maxslary"]
#     companyLogo=resultlist["companyLogo"]
#     companySize=resultlist["companySize"]
#     companyLabelList=resultlist["companyLabelList"]
#     city=resultlist["city"]
#     district=resultlist["district"]
#     businessZones=resultlist["businessZones"]
#     education=resultlist["education"]
#     firstType=resultlist["firstType"]
#     createTime=resultlist["createTime"]

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

###改表
def process_data(list):
       # 参数  tablename ，
       #  print(type(list))
       #  list = json.loads(list)
        # print (type(list))
        result=list["content"]["positionResult"]["result"]

        #  每一条 拿出来 positionId 看有没有  有更新时间 没有录入数据
        for i in result:
            # 有数据返回0 不执行if  没有数据返回1  执行if语句

            if Select_positionidData("lagou",i["positionId"]):
               l=get_usefullist(i)
               InsertData("lagou",l)

def get_usefullist(list):
    dict={}
    dict["companyShortName"]=list["companyShortName"]
    dict["companyFullName"] = list["companyFullName"]
    dict["positionName"] = list["positionName"]
    dict["positionId"] = list["positionId"]
    dict["positionAdvantage"] = list["positionAdvantage"]
    slary =list["salary"]
    dict["salary"] =slary
    #min  max
    minslary,maxslary=split_slary(slary)
    dict["minslary"] = minslary
    dict["maxslary"] = maxslary
    dict["workYear"] = list["workYear"]
    dict["education"] = list["education"]
    dict["city"] = list["city"]
    dict["district"] = list["district"]
    dict["companySize"] = list["companySize"]
    dict["companyLogo"] = "www.lgstatic.com/thumbnail_120x120/"+list["companyLogo"]
    dict["companyLabelList"] = list["companyLabelList"]
    dict["createTime"] = list["createTime"]
    dict["firstType"] = list["firstType"]
    return dict
def InsertData(TableName, dic):
    print (TableName)
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='213', db='lagou', port=3306,charset="utf8")  # 链接数据库
        cur = conn.cursor()
        COLstr = ''  # 列的字段
        ROWstr = ''  # 行字段

        ColumnStyle = 'VARCHAR(70)'
        for key in dic.keys():
            COLstr = COLstr + '' + key + ' '+ColumnStyle + ','
            ROWstr = (ROWstr + '"%s"' + ',') % (dic[key])


        # 推断表是否存在，存在运行try。不存在运行except新建表，再insert
        try:
            cur.execute("SELECT * FROM  %s" % (TableName))
        except :
            print("chuangjianyichang")
            cur.execute("CREATE TABLE %s (%s) DEFAULT CHARSET=utf8;" % (TableName, COLstr[:-1]))
            cur.execute("alter table %s modify column companyLogo VARCHAR(255);" %(TableName))
            cur.execute("alter table %s modify column minslary int(4);" % (TableName))
            cur.execute("alter table %s modify column createTime datetime;" % (TableName))
        try:
            cur.execute("INSERT INTO %s VALUES (%s)" % (TableName, ROWstr[:-1]))
            print ("插了一条")
        except:
            print("插入异常")

        conn.commit()
        cur.close()
        conn.close()

    except :
        print("yichang")
def Select_positionidData(TableName, positionid):
    #有数据返回0 不执行if  没有数据返回1  执行if语句
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='213', db='lagou', port=3306,charset="utf8")  # 链接数据库
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM  %s" % (TableName))
        except :
            print("没这个表兄弟")
            return 1
        try:
            A=cur.execute("Select * from %s where positionid=%s" % (TableName, positionid))
            print (A)
            if A!=0 :
                return 0
            else :
                return 1
        except:
            print("查询异常")
            return 1

        conn.commit()
        cur.close()
        conn.close()

    except :
        print("链接异常")


if __name__ == '__main__':
    city = "上海"
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
    # fopen = open('D:\\pyProject\\toexcl\\lagou-chonggou\\北京1.13pm7\\北京java2.txt', 'r')
    # for eachLine in fopen:
    #     aaa = aaa + eachLine
    # fopen.close()
    #
    # process_data(aaa)



    # #
    # # db_createtable(conn,cur,"lagouchonggou")
    #
    # db_select(conn,cur,3)

    pnlist= get_pnrangelist()
    go_spider(pnlist)
