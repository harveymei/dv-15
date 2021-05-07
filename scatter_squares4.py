#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/7 4:58 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: scatter_squares4.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。
在可视化中，颜色映射用于突出数据的规律。
"""

import matplotlib.pyplot as plt

x_value = list(range(1001))
y_value = [x**2 for x in x_value]

# https://matplotlib.org/stable/tutorials/colors/colormaps.html
# 参数c设置为y值列表，将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色
# 参数cmap指定映射颜色
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
