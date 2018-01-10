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
import datetime
import pymysql
class dealtojson:
    #  按照传过来的salary 字符串 返回 最低的 工资
    def split_slary(self,salary):
         lowsalary,highsalary=salary.split("k-")
         lenhigh = len(highsalary)
         highsalary=highsalary[:lenhigh-1]
         return lowsalary

    #计算 现在时间和数据时间差
    def calculatordatatime(self,nt,datetime):

        #string转 datetime
        a=0
        space = nt - datetime
        if space.days > 7 :
            a=1

        if 1<space.days<7 :
            a=2
        if space.days<=1:
            a= 3

        return a

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', user='root', password='213', db='lagou', charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT * From lagou201801091217")
# .fetchall() 获取全部：
# results = cursor.fetchall()

resultsone  = cursor.fetchall()
db.close()
datalist = []
for i in resultsone:
# 使用 fetchone() 方法获取一条数据
# for i in results:
#
#
#    print ("Database version : %s " ,i)
#slaryleval  等级
    slaryleval= dealtojson.split_slary("ming",i[3])   #向上传
#  max slaryleval   多少行数据   即  columnnum：
    print (slaryleval)
    maxslaaryleval= 0
    if int(slaryleval)>maxslaaryleval:
        maxslaaryleval=slaryleval
#现在时间
    dt =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#变成 datetime类型
    nt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
    print("dddt",type (dt))
# 判断这个数据 在  左中右   哪个位置 ！   左  ： 距离现在 7天以上  中 ：7-1 天   右 2天内
    dtime= dealtojson.calculatordatatime("ming",nt,i[9])
    print("dttime",dtime)
#弄个数组  然后把生成的每一条数据怼进去 datalist

#生成一条局部的数据
    data ={}
    data["i"]=slaryleval
    data["k"]=dtime
    data["labename"] = "label"+str(slaryleval)+str(dtime)
    data["urlpic"]=i[6]
    data["todo"]=i[2]
    datalist.append(data)
print (range(0,3))
# [ for i in range(3)]
# myList = [range (3)for i in range(0,21)]
myList=[[ ] for i in range(20)]
#此处判断 列表长度  如果 大于100 要分页  即 分json文件
for ever in range(len(datalist)):
       i= int(datalist[ever]["i"])
       print (i,"i")
       j= int(datalist[ever]["k"])
       print (j,"j")

       myList[i][j].append(datalist[ever])
print (myList)
print ("!",maxslaaryleval)
# part 2


#解析 获得 上面的数组     创建label  集合

# jsonStr = json.dumps(data)


# 关闭数据库连接
