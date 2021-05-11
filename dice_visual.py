#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/8 5:47 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: dice_visual.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import pygal
from die import Die


# 创建两个实例
die_1 = Die()
# die_2 = Die()
# 投掷两个面数不同骰子
die_2 = Die(10)  # 一个6面，一个10面

# 定义空列表用于存储结果
results = []
# for roll_num in range(1000):
for roll_num in range(50000):  # 修改为摇骰子50000次
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides  # 计算最大面数值
for value in range(2, max_result):  # 遍历最小面数值2到最大面数值之间数值
    frequency = results.count(value)  # 在结果列表中计数面数值出现的次数并赋值变量
    frequencies.append(frequency)  # 将统计结果写入列表

# 可视化结果
hist = pygal.Bar()

# 设置图表样式
# hist.title = "Results of rolling two D6 dice 1000 times."
hist.title = "Results of rolling a D6 and a D10 50,000 times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# hist.add("D6 + D6", frequencies)  # 添加数据系列标签
hist.add("D6 + D6", frequencies)  # 修改标签
hist.render_to_file("dice_visual_05111122.svg")  # 渲染到文件
