#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/7 4:03 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: scatter_squares2.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
使用scatter()绘制一系列点
"""

import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]

plt.scatter(x_value, y_value, s=200)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
