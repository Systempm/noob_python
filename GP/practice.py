# encoding: utf-8

'''
@author: ming2

@contact: 908319305@qq.com

@file: practice.py

@time: 2018/1/31 20:47

@desc:

'''
import pandas as pd
import numpy as np
# df = pd.DataFrame([1, 2, 3, 4, 5], columns=['cols'])
# df.reindex(columns=list('ABCDE'))
# pp=pd.concat([df,pd.DataFrame( columns=['c','asdddd'] )])
# sb=pp.reindex(columns=["1","2","3"])
# for i in range (len(df)):
#     df['cols'][i] = i +1
##上面是 DataFrame 加列   靠的是  列名重排


import math

print ("tan(3) : ",  math.tan(3))
print(   180/math.pi *  math.atan(1))

# 所以    sin30°就得写成 Math.sin（30*Math.PI/180）。其中小括弧内的部分是把30°化为弧度，即30×π/180

# df2 = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['a', 'b', 'c', 'd'], columns=['one', 'two', 'three', 'four'])

