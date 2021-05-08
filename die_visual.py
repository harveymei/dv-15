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
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
