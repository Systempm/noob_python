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

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
class message_url:
    def message_body(self,url,headers):
        response=requests.post(url,headers=headers)
        response.close()#11
        print( type(response))
        m=response.text
        return m

        print (m)






client = MongoClient('localhost', 27017)
db = client.test
account = db.lagou30
def to_dict(list1):
    list2 = ['公司', '职位', '工资', '地点', '特点', 'logo', '公司介绍','详细网址']
    dictlist= dict(zip(list2, list1))
    return dictlist






if __name__ == '__main__':
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
             'Referer': 'http://bzclk.baidu.com/adrc.php?t=06KL00c00f7Ghk600n-u0FNkUsKbP14p00000c5j9db00000V_69gZ.THL0oUhY1x60UWdBmy-bIfK15yPWPHfznWFBnj0sPAuBPhn0IHdKPHF7fWTznjRznYPjwj9afbR1fHNKwHTYrHbsrDPKP0K95gTqFhdWpyfqn10Ln1RzPjRvnzusThqbpyfqnHm0uHdCIZwsrBtEILILQhk9uvqdQhPEUiqBuy-Jpy4MQgGCmyqspy3E5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAn0mLFW5Hnsn1nd&tpl=tpl_10085_15730_11224&l=1502069635&attach=location%3D%26linkName%3D%25E8%25A1%25A8%25E6%25A0%25BC2-2%26linkText%3D%25E5%258C%2597%25E4%25BA%25AC%26xp%3Did(%2522m23a441b3%2522)%252FDIV%255B1%255D%252FDIV%255B1%255D%252FDIV%255B3%255D%252FDIV%255B1%255D%252FTABLE%255B1%255D%252FTBODY%255B1%255D%252FTR%255B1%255D%252FTD%255B2%255D%252FA%255B1%255D%26linkType%3D%26checksum%3D12&ie=utf-8&f=8&tn=baidu&wd=%E6%8B%89%E5%8B%BE%E7%BD%91&oq=%25E7%2588%25AC%25E5%258F%2596%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%2520%25E9%259C%2580%25E8%25A6%2581%25E5%2593%25AA%25E4%25BA%259B%25E6%2595%25B0%25E6%258D%25AE&rqlang=cn&inputT=1316',
             'Origin': 'https://www.lagou.com'
             }
    aaa = 0
    # url1="https://www.lagou.com/beijing-zhaopin/?utm_source=m_cf_cpt_baidu_pc"
    for page in  range (1,30):
        url="https://www.lagou.com/shenyang-zhaopin/{page}/?filterOption={page}".format(page=page)
        a=message_url()
        # data={
        #     "first": 'true',
        #     "pn":  "1",
        #     "kd":  "python",
        #   }
        m=a.message_body(url,headers)
        print (type(m))
        # name= str(page)+".html"
        # f = open(name, 'w', encoding='utf-8')
        # f.write(m)

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
            list = [companyname, positisioniame, salary, location, introduction, logourl, companyinformation, hrefurl]
            account.insert(to_dict(list))
        print("一页完成")
        aaa = aaa + 1
        time.sleep(2)
        print(aaa)