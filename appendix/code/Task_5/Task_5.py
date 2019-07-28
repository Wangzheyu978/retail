# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from tkinter import _flatten
import re
plt.rcParams['font.sans-serif'] = 'SimHei'
data = pd.read_excel('C:/Users/csh/Desktop/douban/aaa.xlsx')
df = pd.DataFrame(data,columns=['rating','time1'])
times = []
score = []
for i in range(0,len(df)):
    times.append(re.findall(r'\d{4}-\d{2}-\d{2}', str(df['time1'][i])))
times = list(_flatten(times))
for j in range(0,len(df)):
    score.append(df['rating'][j])
del score[282]
df=pd.DataFrame(list(zip(score,times)),
                  columns=['rating','time1'])
df['time1'] = pd.to_datetime(df['time1'])
df = df.set_index('time1')
s = pd.Series(df['rating'], index=df.index)
data_1 = df.resample('AS').mean().to_period('A')
f= pd.DataFrame(data_1)
f.to_csv('e.csv')
data_2 = pd.read_csv('e.csv')
plt.figure(figsize=(9,8))
plt.plot(data_2['time1'],data_2['rating'])
plt.xticks(rotation=45)
plt.xlabel('age')
plt.ylabel('rate')
plt.savefig('C:/Users/csh/Desktop/douban/task5_2.jpg')
plt.show()