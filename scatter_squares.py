#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/7 3:10 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: scatter_squares.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
绘制散点图
"""
import matplotlib.pyplot as plt

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter
# x, y: float or array-like, shape (n, )
# The data positions.
# s: float or array-like, shape (n, ), optional
# The marker size in points**2. Default is rcParams['lines.markersize'] ** 2.
# 使用s=200指定标点尺寸
plt.scatter(2, 4, s=200)

# 设置图表标题及坐标轴标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params
# which{'major', 'minor', 'both'}, default: 'major'
# The group of ticks to which the parameters are applied.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
