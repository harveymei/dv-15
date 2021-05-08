#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/8 2:38 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: rw_visual3.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
重新绘制起点和终点
"""


import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:  # 循环
    # rw = RandomWalk()
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口尺寸，单位英寸
    # plt.figure(figsize=(10, 6))
    plt.figure(dpi=128, figsize=(10, 6))

    # plt.scatter(rw.x_values, rw.y_values, s=5)
    # 给点着色，根据点的生成顺序由浅蓝色到深蓝色
    point_numbers = list(range(rw.num_points))  # 生成一个0-4999的列表
    # 向颜色参数c传递列表值，指定颜色映射为蓝色，去除点的黑色轮廓
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点，在已绘制完的点上重新绘制起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    # 以上方法无效
    # gca：Get the current Axes, creating one if necessary.
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n) ")  # 用户输入
    if keep_running == 'n':  # 判断根据用户输入为n时终止并退出程序
        break
