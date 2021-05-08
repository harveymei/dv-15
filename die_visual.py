#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/8 4:45 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: die_visual.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

from die import Die

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

# print(results)
# 打印分析列表
print(frequencies)
