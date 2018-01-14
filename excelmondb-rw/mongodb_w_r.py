import json

import xlrd
from pymongo import MongoClient


class MongoDb:
    #方法1  直接 本地 设置好
    def mongodbtoexcel(self):
        row = 0
        # client = MongoClient('mongodb://username:pwd@192.168.1.22:27017/send_excel')
        client = MongoClient('localhost', 27017)
        db = client.test
        collection = db.items11
        files = collection.find()
        newf = collection.find()
        print('总数：', collection.count())
        import xlrd
        import xlutils.copy
        # 打开一个workbook
        rb = xlrd.open_workbook('E:\\Code\\Python\\test1.xls')
        wb = xlutils.copy.copy(rb)
        # 获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
        ws = wb.get_sheet(0)
        j = 0  # 写入数据
        s = newf.next()
        for title in s.keys():
            if title != "":
                ws.write(row, j, str(title))
                j = j + 1
        for i in files:
            everydata = list(i.values())
            print(everydata)
            for j in range(len(everydata)):
                content = str(everydata[j])
                ws.write(row + 1, j, content)  # 写入单元格
            row = row + 1
        # 利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
        wb.save('E:\\Code\\Python\\test1.xls')
    def exceltomongodb(self):
        # 连接数据库
        client = MongoClient('localhost', 27017)
        db = client.test
        account = db.items11
        data = xlrd.open_workbook('a.xlsx')
        table = data.sheets()[0]
        # 读取excel第一行数据作为存入mongodb的字段名
        rowstag = table.row_values(0)
        nrows = table.nrows
        # ncols=table.ncols
        # print rows
        returnData = {}
        for i in range(1, nrows):
            # 将字段名和excel数据存储为字典形式，并转换为json格式
            returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))
            # 通过编解码还原数据
            returnData[i] = json.loads(returnData[i])
            # print returnData[i]
            account.insert(returnData[i])

    ##带有修改参数的方法
    def mongodbtoexcel(self,excelurl=None):
        if excelurl==None:
            excelurl='E:\\Code\\Python\\test1.xls'
        row = 0
        # client = MongoClient('mongodb://username:pwd@192.168.1.22:27017/send_excel')
        client = MongoClient('localhost', 27017)
        db = client.test
        collection =                           db.items11
        files = collection.find()
        newf = collection.find()
        print('总数：', collection.count())
        import xlrd
        import xlutils.copy
        # 打开一个workbook
        rb = xlrd.open_workbook(excelurl)
        wb = xlutils.copy.copy(rb)
        # 获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
        ws = wb.get_sheet(0)
        j = 0  # 写入数据
        s = newf.next()
        for title in s.keys():
            if title != "":
                ws.write(row, j, str(title))
                j = j + 1
        for i in files:
            everydata = list(i.values())
            print(everydata)
            for j in range(len(everydata)):
                content = str(everydata[j])
                ws.write(row + 1, j, content)  # 写入单元格
            row = row + 1
        # 利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
        wb.save(excelurl)