#*-* coding:utf-8 *-*

'''
@author: ming2

@contact: 908319305@qq.com

@file: bs4a.py

@time: 2017/12/24 11:18

@desc:
一般都存在html 中 不是xml  马蛋——））
'''


from pymongo import MongoClient
from bs4 import BeautifulSoup


client = MongoClient('localhost', 27017)
db = client.test
account = db.lagougou
def to_dict(list1):
    list2 = ['公司', '职位', '工资', '地点', '特点', 'logo', '公司介绍','详细网址']
    dictlist= dict(zip(list2, list1))
    return dictlist





htmlfile = open('new.html', 'r',encoding= 'utf-8')#1
htmlpage = htmlfile.read()

soup = BeautifulSoup(htmlpage, "html.parser")  #实例化一个BeautifulSoup对象
print (soup.title.string)
# producer_entries = soup.find("li",{"class":"con_list_item default_list"})
# print ('位置',producer_entries.span.text)  #1111
# # re.producer_entries.span(<:')
# producer_entries.span.name = "sss"
# print ('时间',producer_entries.span)
'''
producer_entries = soup.find("li",{"class":"con_list_item default_list"})
print(producer_entries.atrrs)
print(producer_entries)

producer_entries = soup.find("li",{"class":"con_list_item default_list"})
soup1 = BeautifulSoup(producer_entries,features="xml")
print (soup1.find("span ",{"class":"add"}))
'''
# print(soup.find("li",{"class":"con_list_item default_list"}).a.string)
# print (soup.a.string)
# print (producer_entries.string)!!!#1
# print( producer_entries)


# producer_entries = soup.find("a",{"class":"position_link"})
# print(producer_entries)
soupp=soup(class_="con_list_item default_list")
urlsoup = soup.find_all("a",{"class":"position_link"})
locationsoup = soup.find_all("span",{"class":"add"})
timesoup=soup.find_all("span",{"class":"format-time"})
experience=soup.find_all("div",{"class":"p_bot"})  # 手动 拆分 薪水和 年限把11
companyinformationsoup=soup.find_all("div",{"class":"company_name"})#  里面有公司的网页 ！@#@#！@#￥
companyspecial=soup.find_all("div",{"class":"industry"})
logourlsoup=soup.find_all("div",{"class":"com_logo"})
introductionsoup=soup.find_all("div",{"class":"li_b_r"})
# print (introductionsoup[1].text)
# print (logourlsoup[1].a.attrs['href'])
# print (companyspecial[1].text)


# print (experience[1])
# print (experience)
# print (len(experience))
# print (experience.text)
# print("span class money",timesoup)
# print (urlsoup)
# print(type(soupp))
# print (len(soupp))
te=[]
for i in range (len(soupp)):
     companyname = soupp[i].attrs['data-company']
     salary = soupp[i].attrs['data-salary']
     positisioniame = soupp[i].attrs['data-positionname']
     location = locationsoup[i].text  # ????
     introduction = introductionsoup[i].text
     logourl = logourlsoup[i].img.attrs['src']
     companyinformation = companyinformationsoup[i].a.attrs['href']
     hrefurl = urlsoup[i].attrs['href']
     list = [companyname, positisioniame, salary, location, introduction, logourl, companyinformation, hrefurl]
     account.insert(to_dict(list))



# companyname=soupp[1].attrs['data-company']
# salary=soupp[1].attrs['data-salary']
# positisioniame=soupp[1].attrs['data-positionname']
# location = locationsoup[1].text  #  ????
# introduction=introductionsoup[2].text
# logourl = logourlsoup[1].img.attrs['src']
# companyinformation=companyinformationsoup[1].a.attrs['href']
# hrefurl=urlsoup[1].attrs['href']
# list=[companyname,positisioniame,salary,location,introduction,logourl,companyinformation,hrefurl]
# print (list)
print("____________________________________________")