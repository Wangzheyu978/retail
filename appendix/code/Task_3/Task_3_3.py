import pandas as pd
import matplotlib.pyplot as plt
import csv
df=pd.read_csv('C:/Users/csh/Desktop/douban/aaa.csv',encoding='utf-8')
df['time']=pd.to_datetime(df['time'])
df = df.set_index('time')
f=df.resample('D').mean()
f= f.fillna(0)
f.to_csv('d.csv',encoding='utf-8_sig')
e=pd.read_csv('d.csv')
plt.plot(e['time'],e['rating'])
plt.xticks(rotation=45)
plt.xlabel('Day')
plt.ylabel('Mean')
plt.savefig('C:/Users/csh/Desktop/douban/task3_3.jpg')
plt.show()
print(f)


