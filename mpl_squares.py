#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/7 11:34 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: mpl_squares.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
Visualization with Python¶
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
"""

# https://matplotlib.org/stable/api/pyplot_summary.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
# 导入模块并设置别名
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()
