import pandas as pd
import matplotlib.pyplot as plt
import csv
df=pd.read_csv('C:/Users/csh/Desktop/douban/aaa.csv',encoding='utf-8')
df['time']=pd.to_datetime(df['time'])
df = df.set_index('time')
s = pd.Series(df['name'], index=df.index)
f=df.resample('D').count()
f.to_csv('c.csv',encoding='utf-8_sig')
e=pd.read_csv('c.csv')
plt.plot(e['time'],e['name'])
plt.xticks(rotation=45)
plt.xlabel('Day')
plt.ylabel('Count')
plt.savefig('C:/Users/csh/Desktop/douban/task3_1.jpg')
plt.show()

