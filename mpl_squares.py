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
# 调用plt.plot方法并传入参数，绘制默认风格和颜色的线条
# Line width, in points.
# 使用linewidth指定线条宽度点数
# https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth
plt.plot(squares, linewidth=5)

# 设置图表标题并设置坐标轴刻度
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel
# https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
# tick_params
# Change the appearance of ticks, tick labels, and gridlines.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params
# 同时应用于x坐标轴和y坐标轴
plt.tick_params(axis='both', labelsize=14)

# Display all open figures.
# 显示图形
plt.show()
