import pandas as pd
import matplotlib.pyplot as plt
import csv
import re
import numpy as np
import pickle
import datetime
from pandas import  to_datetime
df=pd.read_csv('C:/Users/csh/Desktop/douban/aaa.csv',encoding='utf-8')
df=to_datetime(df['time'])
s_t=df.dt.hour
result=[]

arr = np.array(s_t)
key = np.unique(arr)
result = []
result1=[]
for k in key:
    mask = (arr == k)
    arr_new = arr[mask]
    v = arr_new.size
    result.append(v)
    result1.append(k)

plt.plot(result1,result)
plt.xticks(rotation=45)
plt.xlabel('Hour')
plt.ylabel('Count')
plt.savefig('C:/Users/csh/Desktop/douban/task3_2.jpg')
plt.show()

