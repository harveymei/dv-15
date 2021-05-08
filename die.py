#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/8 4:23 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: die.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
投掷骰子
"""

from random import randint


# 创建Die类
class Die:
    # 方法__init__()接受一个可选参数。创建这个类的实例时，如果没有指定任何实参，面数默
    # 认为6；如果指定了实参，这个值将用于设置骰子的面数。
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    # 方法roll()使用函数randint()来返回一个1和面数之间的随机数。
    def roll(self):
        return randint(1, self.num_sides)
