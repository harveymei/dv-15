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
# plt.scatter(x_value, y_value, s=40)
#
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter
# 删除数据点轮廓，默认为蓝色点黑色轮廓
# plt.scatter(x_value, y_value, edgecolors='none', s=40)
# 自定义点的颜色
# plt.scatter(x_value, y_value, c='red', edgecolors='none', s=40)
# 使用RGB值自定义点的颜色
# 使用元组分别表示红绿蓝分量
# 值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅
plt.scatter(x_value, y_value, c=(0, 0, 0.8), edgecolors='none', s=40)

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
