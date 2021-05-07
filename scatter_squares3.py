#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/7 4:10 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: scatter_squares3.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
使用循环自动计算数据
"""

import matplotlib.pyplot as plt

# 使用range()函数生成1-1000数值列表赋值变量
x_value = list(range(1, 1001))
# 遍历x值并进行平方运算后赋值变量
y_value = [x**2 for x in x_value]

# 绘图
plt.scatter(x_value, y_value, s=40)

# 设置图表标题及坐标轴标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴取值范围
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis
# xmin, xmax, ymin, ymaxfloat, optional
# The axis limits to be set. This can also be achieved using
plt.axis([0, 1100, 0, 1100000])

plt.show()
