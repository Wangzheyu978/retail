import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='SimHei'
c=pd.read_csv('C:/Users/csh/Desktop/douban/aaa.csv')
df=pd.DataFrame(c,columns=['rating','location'])
data=pd.pivot_table(df[['location','rating']],index='location',aggfunc=np.mean)
# data.to_csv('e.csv',encoding='utf_8_sig')
e=pd.read_excel('C:/Users/csh/Desktop/douban/e.xlsx')
plt.plot(e['location'],e['rating'])
plt.xticks(rotation=45)
plt.xlabel('Day')
plt.ylabel('Count')
plt.savefig('C:/Users/csh/Desktop/douban/task4_2.jpg')
plt.show()