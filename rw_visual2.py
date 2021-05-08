#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/8 10:56 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: rw_visual2.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
多次运行随机漫步
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:  # 循环
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=5)
    plt.show()

    keep_running = input("Make another walk? (y/n) ")  # 用户输入
    if keep_running == 'n':  # 判断根据用户输入为n时终止并退出程序
        break
