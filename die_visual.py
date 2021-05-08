#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/8 4:45 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: die_visual.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

from die import Die
# 绘制直方图，引入模块
import pygal


# 调用类，创建实例
die = Die()

# 定义空列表存储结果
results = []
# 定义for循环，调用roll方法输出结果并将结果存入列表
# for roll_num in range(100):
# 增加投掷次数进行分析
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析
# 定义列表存储分析结果
frequencies = []

# 定义循环
for value in range(1, die.num_sides+1):  # 骰子面数+1即1-6之间
    frequency = results.count(value)  # 计数结果列表中的特定骰子数值赋值变量
    frequencies.append(frequency)  # 将计数结果一次写入分析列表

# 对结果进行可视化
hist = pygal.Bar()  # 实例化类

# http://www.pygal.org/en/stable/documentation/configuration/title.html#title
# http://www.pygal.org/en/stable/documentation/configuration/label.html#x-labels
#
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency Result"

# http://www.pygal.org/en/stable/documentation/configuration/serie.html#options
# http://www.pygal.org/en/stable/documentation/output.html#file
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

# print(results)
# 打印分析列表
# print(frequencies)
