# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: gpf.py

@time: 2018/1/31 10:32

@descd:

'''
import pandas
import tushare
import math
print(tushare.__version__)


import tushare as ts
import pandas as pf

#
# for i in  range (600000,600040):
#     basestation = "F:\\GPDATA\\{}.csv".format(i)
#     df=ts.get_k_data(str(i),  start='2017-6-01', end='2018-1-31' )
#     df.to_csv(basestation, encoding='utf-8')

#
i = 600917

basestation = "F:\\GPDATA\\{}.csv".format(i)
df=ts.get_k_data(str(i))
sp=df.reindex(columns=["date","open","close","high","low","volume","code","ocup","ocdown","upk","downk","upd","downd"])


for  i  in range (len (sp)):
    if sp['open'][i]>sp['close'][i]:
        sp['ocup'][i]=sp['open'][i]
        sp['ocdown'][i] = sp['close'][i]
    else:
        sp['ocup'][i] = sp['close'][i]
        sp['ocdown'][i] = sp['open'][i]

for b  in  range (1,len(sp)):
       upk = sp['ocup'][b]-sp['ocup'][b-1]
       sp['upk'][b]  = upk
       downk = sp['ocdown'][b]-sp['ocdown'][b-1]
       sp['downk'][b]= downk
       sp["upd"][b]= 180/math.pi *  math.atan(upk )
       sp["downd"][b]= 180/math.pi *  math.atan(downk )
print(sp)
# df=ts.get_k_data(str(i),start='2016-01-01')

basestation ="F:\\GPDATA\\b.csv"
sp.to_csv(basestation, encoding='utf-8')

# ts.get_k_data("600000", index=True,start='2017-6-01', end='2018-1-31')
# basestation ="F:\\GPDATA\\a.csv"
#
# df = ts.get_k_data('600050')
# #直接保存
# df.to_csv(basestation, encoding='utf-8')

#设定数据位置（从第3行，第6列开始插入数据）
