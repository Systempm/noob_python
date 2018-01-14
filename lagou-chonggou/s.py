# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: s.py

@time: 2018/1/13 5:46

@desc:

'''
# -*-coding:utf-8-*-
import csv
import json
import requests
import sys

#解决编码问题
# reload(sys)
# sys.setdefaultencoding('utf-8')

#获取json数据
def get_json_data(city,position,page):
    #请求拉勾的职位查询接口，返回的是json格式数据
    #url=" https: // www.lagou.com / jobs / list_{}?city ={}& cl = false & fromSearch = true & labelWords = & suginput =".format(position,city)
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false'.format(city)
    data = {
        'first':'ture',
        'pn':page,
        'kd':position
    }
    # header 里面加cookie就可以防止被ban
    headers = {
"Accept:application/json, text/javascript, */*; q=0.01"
"Accept-Encoding:gzip, deflate, br"
"Accept-Language:zh-CN,zh;q=0.8"
"Connection:keep-alive"
"Content-Length:23"
"Content-Type:application/x-www-form-urlencoded; charset=UTF-8"
"Cookie:user_trace_token=20180112203339-3be4004e-a0d5-4156-bf0e-5c046af4e618; "
"__guid=237742470.2605937090993304600.1515760413772.495; "
"LGUID=20180112203340-d1cd8b7d-f794-11e7-a2ab-5254005c3644; "
"JSESSIONID=ABAAABAAAGFABEF5FE7D1E04AAB29D57DA99D03DCDB9F33; "
"PRE_UTM=; PRE_HOST=www.baidu.com; "
"PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dg87l8AIIj_rluAiRfSyPdXc6ad0IbFL7YiS8PxTYJN3%26wd%3D%26eqid%3D88f80f4300015b55000000035a592d78; "
"PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; "
"index_location_city=%E5%85%A8%E5%9B%BD; "
"TG-TRACK-CODE=index_search; "
"X_HTTP_TOKEN=b45496bd79dcd7ed322dd73e5171e835; "
"_gid=GA1.2.928823699.1515760415; "
"_ga=GA1.2.50887905.1515760415; "
"LGSID=20180113054948-82707980-f7e2-11e7-93d3-525400f775ce; "
"LGRID=20180113060746-057201ab-f7e5-11e7-a2e1-5254005c3644; "
"Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515760415,1515793781;"
"Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515794861; "
"SEARCH_ID=baf015ec9ee84c419a20120f9fbc3bbc; "
"monitor_count=38"
"Host:www.lagou.com"
"Origin:https://www.lagou.com"
"Referer:https://www.lagou.com/jobs/list_java?city=%E6%B2%88%E9%98%B3&cl=false&fromSearch=true&labelWords=&suginput="
"User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
"X-Anit-Forge-Code:0"
"X-Anit-Forge-Token:None"
"X-Requested-With:XMLHttpRequest"


    }
    response = requests.post(url,headers=headers,data=data)
    print (response.text)
    return response.text

#获取最大页数
def get_max_pageNumber(city,position):
    # 请求职位查询接口，用总条数除以每页的条数15，得到总页数
    result = get_json_data(city,position,'1')
    pageNumber = int(json.loads(result)['content']['positionResult']['totalCount']/15)
    return pageNumber

#从json数据里面获取想要的字段
def get_positon_results(json_data):
    data = json.loads(json_data)
    #状态是成功的再处理
    if data['success'] == True:
        position_results = []
        positions = data['content']['positionResult']['result']
        for item in positions:
            companyShortName = item['companyShortName']
            companyFullName = item['companyFullName']
            companySize = item['companySize']
            positionName = item['positionName']
            workYear = item['workYear']
            salary = item['salary']
            industryField = item['industryField']
            financeStage = item['financeStage']
            createTime = item['createTime']
            education = item['education']
            district = item['district']
            positionId = item['positionId']
            jobNature = item['jobNature']
            positionAdvantage = item['positionAdvantage']
            positionUrl = 'https://www.lagou.com/jobs/' + str(positionId) + '.html'


            position_results.append([companyFullName,positionName,workYear,salary,industryField,financeStage,
                                     companyShortName,companySize,createTime,education,district,jobNature,
                                     positionAdvantage,positionId,positionUrl])
        return position_results
    else:
        print ('数据出错了...')

def writeCSV(file,data_list):
    with open(file,'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['公司名称','职位名称','工作年限','薪资范围','行业','融资情况',
                         '公司简称','公司规模','发布时间','学历要求','地区','工作性质','职位优势','职位ID','职位链接'])
        for data in data_list:
            for row in data:
                writer.writerow(row)


def main():
    city = "沈阳"
    position = "java"
    fileName = "javaa"
    filePath = 'D:\\' + fileName + '.csv'
    pageNumber = get_max_pageNumber(city,position)
    positions = []
    for i in range(1,pageNumber + 1):
        print ('开始爬第{}页...'.format(i))
        page_data = get_json_data(city,position,str(i))
        page_result = get_positon_results(page_data)
        positions.append(page_result)

    writeCSV(filePath,positions)

if __name__ == '__main__':
    get_json_data("沈阳","java",2)
