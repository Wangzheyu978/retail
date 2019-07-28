# coding=gbk
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
from pyecharts import Geo ,Map
df=pd.read_csv('C:/Users/csh/Desktop/douban/aaa.csv',encoding='utf-8')
arr = df['location']
key = np.unique(arr)
result =[]
result1=[]
data=[]
for k in key:
    if '\u4e00' <= k <= '\u9fff':
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result=k
        result1=v
        data.append([result,result1])
        df = pd.DataFrame(data, columns=['city','count'])
        df.to_csv('a.csv', encoding='utf_8_sig')
    else:
        continue

e=pd.read_csv('a.csv')
geo = Geo("居住地", "location", title_color="#fff",
          title_pos="center", width=1000,
          height=600, background_color='#404a59')
geo.add("", e['city'], e['count'], visual_range=[0, 200], maptype='china',visual_text_color="#fff",
        symbol_size=10, is_visualmap=True)
geo.render("居住地.html")
geo

