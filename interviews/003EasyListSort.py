#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简洁的代码实现: int list1大于100的元素存入list2, list2逆序排序
"""


def find_bigger_reserve(list1):
    list2 = list()
    for i in range(len(list1)):
        if list1[i] > 100:
            list2.append(list1[i])
    # list2 = sorted(list2, reverse=True)
    list2.sort(reverse=True)
    return list2


if __name__ == '__main__':
    result = find_bigger_reserve([123, 23, 233, 34, 121, 122, 1333])
    print(result)



