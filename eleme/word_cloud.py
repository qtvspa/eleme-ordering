# -*- coding:utf-8 -*-

import jieba
from random import randint
from matplotlib import pyplot as plt
from wordcloud import WordCloud

from eleme.utils import clean_data


def random_color(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):

    """Random Color func"""
    r = randint(30, 255)
    g = randint(30, 180)
    b = int(100.0 * float(randint(60, 120)) / 255.0)
    return "rgb({:.0f}, {:.0f}, {:.0f})".format(r, g, b)


if __name__ == '__main__':

    df = clean_data('ele_0715.txt')
    foods_list = [f for f in df['foods']]
    foods = ''.join(foods_list)
    after_jieba_data = jieba.cut(foods, cut_all=True)
    words = ' '.join(after_jieba_data)

    wc = WordCloud(background_color="white",
                   width=1000,
                   height=600,
                   font_path='/System/Library/Fonts/PingFang.ttc', # 字体文件可自行更换路径
                   color_func=random_color).generate(words)
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig('a.png', format='png', dpi=200)