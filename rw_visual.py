#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/8 10:28 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: rw_visual.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
绘制图形
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建RandomWalk实例，并将生成的点绘制出来
rw = RandomWalk()
rw.fill_walk()  # 调用方法生成坐标值列表

# 绘制图形
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
plt.savefig('rw_visual_05081033.png')
