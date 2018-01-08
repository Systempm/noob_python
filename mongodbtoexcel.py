from pymongo import MongoClient
row=0
#client = MongoClient('mongodb://username:pwd@192.168.1.22:27017/send_excel')
client = MongoClient('localhost', 27017)
db = client.test
collection = db.items11
files = collection.find()
newf = collection.find()
print('总数：', collection.count())
import xlrd
import xlutils.copy
#打开一个workbook
rb = xlrd.open_workbook('E:\\Code\\Python\\test1.xls')
wb = xlutils.copy.copy(rb)
#获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
ws = wb.get_sheet(0)
j=0#写入数据
s = newf.next()
for title in s.keys():
    if title!="":
        ws.write(row, j, str(title))
        j=j+1
for i in files:
    everydata = list(i.values())
    print (everydata)
    for j in  range(len(everydata)):
        content=str(everydata[j])
        ws.write(row+1,j,content)  #写入单元格
    row = row + 1
#利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
wb.save('E:\\Code\\Python\\test1.xls')