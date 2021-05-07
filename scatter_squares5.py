#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/7 6:03 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: scatter_squares5.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import matplotlib.pyplot as plt

x_value = list(range(6))
# x_value = list(range(5001))
y_value = [x**3 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Purples, edgecolors='none', s=40)

plt.title("Cube Numbers", fontsize=22)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cube of Value", fontsize=12)

plt.tick_params(axis='both', which='major', labelsize=12)
plt.axis([0, 6, 0, 130])
# plt.axis([0, 5010, 0, 125000001000])

# plt.show()
plt.savefig('cube_numbers.png')
