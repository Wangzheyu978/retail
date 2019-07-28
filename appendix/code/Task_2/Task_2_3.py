import jieba
import pandas as pd
with open('C:/Users/csh/Desktop/douban/cc.txt','r',encoding='utf-8')as f:
    txt=f.read()
txt=txt.split()
cut_text=[jieba.lcut(x)for x in txt]
all_words=[]
for i in cut_text:
    all_words.extend(i)
df = pd.DataFrame(all_words)
print(df)
df.to_csv('C:/Users/csh/Desktop/douban/cp.csv', encoding='utf_8_sig')