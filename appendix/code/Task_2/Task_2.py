from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import  jieba
def GetWordCloud():
    path_txt = 'C:/Users/csh/Desktop/douban/aa.txt'
    path_img = "C:/Users/csh/Desktop/douban/1.jpg"
    f = open(path_txt, 'r', encoding='UTF-8').read()
    background_image = np.array(Image.open(path_img))
    cut_text = " ".join(jieba.cut(f))
    wordcloud = WordCloud(
       font_path="C:/Windows/Fonts/simfang.ttf",
       background_color="white",
       mask=background_image).generate(cut_text)
    image_colors = ImageColorGenerator(background_image)
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.savefig('C:/Users/csh/Desktop/douban/p.jpg')
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
   GetWordCloud()


