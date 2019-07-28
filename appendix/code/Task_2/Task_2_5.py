import pandas as pd
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import  jieba
import json
csv_file = "C:/Users/csh/Desktop/douban/movie.csv"
csv_data = pd.read_csv(csv_file, low_memory = False)#防止弹出警告
df = pd.DataFrame(csv_data,columns=['comment','rate'])
a=df.loc[df['rate'].str.contains('荐'),['comment']]
b=df.loc[df['rate'].str.contains('还行'),['comment']]
c=df.loc[df['rate'].str.contains('差'),['comment']]
a.to_csv('C:/Users/csh/Desktop/douban/a1.txt', sep='\t', index=False)
b.to_csv('C:/Users/csh/Desktop/douban/a2.txt', sep='\t', index=False)
c.to_csv('C:/Users/csh/Desktop/douban/a3.txt', sep='\t', index=False)
print(len(a))
print(len(b))
print(len(c))
def GetWordCloud():
    for i in range(1,4):
        path_txt = 'C:/Users/csh/Desktop/douban/a{}.txt'.format(i)
        path_img = "C:/Users/csh/Desktop/douban/aixin.jpg"
        f = open(path_txt, 'r', encoding='UTF-8').read()
        background_image = np.array(Image.open(path_img))
        print(type(f))
        cut_text = " ".join(jieba.cut(f))
        wordcloud = WordCloud(
           font_path="C:/Windows/Fonts/simfang.ttf",
           background_color="white",
           mask=background_image).generate(cut_text)
        image_colors = ImageColorGenerator(background_image)
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
        plt.savefig('C:/Users/csh/Desktop/douban/p{}.jpg'.format(i))
        plt.axis("off")
        plt.show()


if __name__ == '__main__':
   GetWordCloud()



