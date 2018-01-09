# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: dealsqltojson.py

@time: 2018/1/9 21:00

@desc:

'''
# 写文件
# with open("douban.txt", "w") as f:
#     f.write("这是个测试！1")
#

import pymysql
class dealtojson:
    def split_slary(self,salary):
         lowsalary,highsalary=salary.split("k-")
         lenhigh = len(highsalary)
         highsalary=highsalary[:lenhigh-1]
         return lowsalary
# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', user='root', password='213', db='lagou', charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT * From lagou201801091217")
# .fetchall() 获取全部：
# results = cursor.fetchall()

resultsone  = cursor.fetchone()

# 使用 fetchone() 方法获取一条数据
# for i in results:
#
#
#    print ("Database version : %s " ,i)
#slaryleval  等级
slaryleval= dealtojson.split_slary("ming",resultsone[3])   #向上传
print (resultsone)
# 关闭数据库连接
db.close()