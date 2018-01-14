# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: newbs4.py

@time: 2017/12/24 20:35

@desc:

'''
from bs4 import BeautifulSoup

htmlfile = open('new.html', 'r',encoding= 'utf-8')#1
htmlpage = htmlfile.read()

soup = BeautifulSoup(htmlpage, "html.parser")
producer_entries = soup.find("li",{"class":"con_list_item default_list"})

tag1=producer_entries
print(tag1.attrs)
print(producer_entries.atrrs)#!!!!!!! attrs
# time = soup.find("span",{"class":"format-time"}).text
# print (time)

# company=producer_entries.atrrs['data-company']
# salary=producer_entries.atrrs['data-salary']
# positionname=producer_entries.atrrs['data-positionname']

# position = soup.find("span",{"class":"add"}).text
# time = soup.find("span",{"class":"format-time"}).text
# money = soup.find("span",{"class":"format-time"}).text
# url=soup.find("a",{"class":"position_link"}).atrrs['href']
# print (soup,producer_entries,company,salary,positionname,position,time,money,url)
#       salary=one.atrrs['data-salary']
#       positionname=one.atrrs['data-positionname']  #网址
        # position_link=one.a.attrs['position_link']
        # local=one.span.text  #位置
        # one.span="sss"
        # time=one.span.text    #发布时间
#         one.span="sss1"
#         education=one.div.text #学历 貌似配不上
#         url = one.a.attrs['company_name']

