# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: daterequest.py

@time: 2018/1/12 20:48

@desc:

'''

url = 'https://www.lagou.com/jobs/positionAjax.json'
para = {'first': 'true','pn': '1', 'kd': kd, 'city': city}
def getInfo(url, para):
    """
    获取信息
    """
    generalHttp = Http()
    htmlCode = generalHttp.post(url, para=para, headers=hd, cookies=ck)
    generalParse = Parse(htmlCode)
    pageCount = generalParse.parsePage()
    info = []
    for i in range(1, pageCount+1):
        print('第%s页' % i)
        para['pn'] = str(i)
        htmlCode = generalHttp.post(url, para=para, headers=hd, cookies=ck)
        generalParse = Parse(htmlCode)
        info = info + getInfoDetail(generalParse)
        time.sleep(2)
    return info