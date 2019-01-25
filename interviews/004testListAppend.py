#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func(t=[], s=''):
    t.append('x')
    s += 'test'
    print(t)
    print(s)


"""
使用默认参数，列表在原来地址，赋值递增; 字符串是重新赋予新的地址和值
['x']
['x', 'x']
['x', 'x', 'x']
"""
for _ in range(3):
    func()


"""
使用自己的参数，列表，字符串都是重新赋予新的地址和值
['x']
['x']
['x']
"""
for _ in range(3):
    func([], '')
