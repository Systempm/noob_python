
#函数必须接收一个'''可迭代对象'''参数，每次调用的时候，返回可迭代对象的下一个元素。
# 如果所有元素均已经返回过，__则抛出StopIteration 异常。
# a = iter('abcd')
# print (next(a))
# print (next(a))
# print (a)

# offset = 1
# a= "woacaocaocaocoa={offset}".format(offset=offset)
# a=a.format(offset=offset)
# print (a)
# page =  111
# name = str(page )+ ".html"
# print (name)




# def file_open(url='F:\\new.xml'):
#     fopen = open(url, 'r')
#     for eachLine in fopen:
#         print(type(eachLine))
#         aa = eachLine
#         print("ka")
#         print("读取到得内容如下：", eachLine)
#         print("ka___________________________")
#     fopen.close()
# file_open()

# print ("1")
# print (aa)
# aa=eval(aa)#1
# print (aa['hahaha'])
# print (type(aa))
import pymongo

'''
for item in collection.find():
    print ("111")
    print (item)
'''
# from pymongo import MongoClient
# names=locals()
#
# client = MongoClient('localhost', 27017)
# db = eval("client.test")
#
# account = eval("db.lagou30")
# for items in account.find():
#     print ("11")
#     print (items)

'''
db=client.test
#连接所用集合，也就是我们通常所说的表，items为表名
collection=db.items

#接下里就可以用collection来完成对数据库表的一些操作
print("111") 
for item in collection.find():
    print ("111")
    print (item)
'''
class sa :
    def message_body(self, a=3):
        print (a)
sa .message_body("asa",a=6)
