# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: cnmbs.py

@time: 2017/12/24 21:39

@desc:

'''
from pymongo import MongoClient

import  mongodb_w_r
def  remove_space(str):
    str=str.split(" ")
    newlist = []
    for i in str :
         if i !="" and i !='/':
             newlist.append(i)
    return (cut_str(newlist))

def cut_str(list1):#remove /n   并且 强制 压缩为8个元素   第9个元素 后面添加 url网站地址
    lend=len(list1)
    print (lend)
    ll=[]#lastlist
    if lend == 6:
        for i in range (len(list1) ):
           if i ==0:
               xx=list1[i].split("\n")
               for s in xx :
                   if s !="\n"and s!="":
                      ll.append(s)
           else:
               xx2=list1[i].split("\n")
               for s in xx2:
                   if s !="\n"and s!="":
                       ll.append(s)
    else :
         print ("数据去空格后 格式不对")
         return None
         list1
    q = []  #把符合条件的数组 压缩到7个元素
    for m in range (8):
        if m <7:
            q.append(ll[m])
        else:
            g=[]
            for loops in  range(len(ll)-7):
                a = 7+int(loops)
                g.append( ll[a])#1
            # ''.join(map(str, a))
            q.append(''.join(map(str, g)))
            # q.append(g)
    # q.append(list[0] + list[1] + list[2])
    return q

def to_dict(list1):
    list2 = ['职位', '地点', '发布时间', '工资', '需要经验', '学历', '公司名称','介绍','网址']
    dictlist= dict(zip(list2, list1))
    return dictlist
# for one in soup(class_="con_list_item default_list"):
#      print(producer_entries.text)
from bs4 import BeautifulSoup
htmlfile = open('new.html', 'r',encoding= 'utf-8')#1
htmlpage = htmlfile.read()
soup = BeautifulSoup(htmlpage, "html.parser")
producer_entries = soup.find("li",{"class":"con_list_item default_list"})

client = MongoClient('localhost', 27017)
db = client.test
account = db.lagou

for one in soup(class_="con_list_item default_list"):
    te = one.text
    te = remove_space(te)
    urll = one.a.attrs['href']
    te.append(urll)
    print (te)
    # account.insert(to_dict(te))


