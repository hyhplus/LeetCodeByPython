#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func(t=[]):
    t.append('x')
    print(t)


"""
使用默认参数，列表在原来地址，赋值递增
['x']
['x', 'x']
['x', 'x', 'x']
"""
for _ in range(3):
    func()


"""
使用自己的参数，列表重新赋予新的地址和值
['x']
['x']
['x']
"""
for _ in range(3):
    func([])
