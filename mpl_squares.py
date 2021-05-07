#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/7 11:34 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: mpl_squares.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
Visualization with Python
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
"""

# https://matplotlib.org/stable/api/pyplot_summary.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show
# 导入模块并设置别名
import matplotlib.pyplot as plt

# 赋值列表
squares = [1, 4, 9, 16, 25]

# Plot y versus x as lines and/or markers.
# 调用plt.plot方法并传入参数
plt.plot(squares)
# Display all open figures.
# 显示图形
plt.show()
