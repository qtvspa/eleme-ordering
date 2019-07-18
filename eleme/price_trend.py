# -*- coding:utf-8 -*-

from eleme.utils import clean_data
from matplotlib import pylab, pyplot as plt
import matplotlib as mpl
import numpy as np


if __name__ == '__main__':

    data = clean_data('ele_0715.txt')
    x = [i for i in range(len(data.price))]
    y = data.price

    # plt.plot(x, data.deliver_fee)
    plt.ylabel("The unit price")
    plt.xlabel("Times")
    plt.plot(x, y)
    # 添加拟合曲线
    func = np.polyfit(x, y, 1)
    f = np.poly1d(func)
    mpl.pylab.plot(x, f(x), "r--")
    plt.show()

