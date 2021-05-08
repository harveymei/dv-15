#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/8 9:23 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: random_walk.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
随机漫步
"""

# https://docs.python.org/3/library/random.html
# https://docs.python.org/3/library/random.html#random.choice
# Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
# 从非空序列中返回随机元素
from random import choice


# PyCharm: Remove redundant parentheses
# class RandomWalk():
class RandomWalk:

    def __init__(self, num_points=5000):
        # 初始化随机漫步属性
        self.num_points = num_points  # 初始点数值

        self.x_values = [0]  # 初始x值
        self.y_values = [0]  # 初始y值

    def fill_walk(self):

        # 不断漫步，直到达到指定列表长度
        while len(self.x_values) < self.num_points:  # 计算列表中存储的不为0的坐标值的数量并比较

            # 决定前移动向及移动的距离
            x_direction = choice([1, -1])  # 随机选择x坐标向右或向左
            x_distance = choice([0, 1, 2, 3, 4])  # 随机选择移动距离
            x_step = x_direction * x_distance  # 移动距离为方向（正负值）与移动距离的乘积

            y_direction = choice([1, -1])  # 随机选择y坐标向上或向下
            y_distance = choice([0, 1, 2, 3, 4])  # 随机选择移动距离
            y_step = y_direction * y_distance  # 移动距离为方向（正负值）与移动距离的乘积

            # 拒绝原地踏步（即随机移动距离为0时继续循环）
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            next_x = self.x_values[-1] + x_step  # 列表中最后一个x坐标值加上移动距离赋值给新变量
            next_y = self.y_values[-1] + y_step  # 列表中最后一个y坐标值加上移动距离赋值给新变量

            self.x_values.append(next_x)  # 将新的x坐标值存入列表末端
            self.y_values.append(next_y)  # 将新的y坐标值存入列表末端
