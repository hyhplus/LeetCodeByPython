#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
查询算法：

最小项搜索
顺序搜索
二分（叉）搜索
hash搜索

"""


def min_search(items):
    """
    最小项搜索
    :param items:
    :return:
    """
    min_index = 0
    for i in range(len(items)):
        if items[min_index] > items[i]:
            min_index = i
    return 'min index：{}'.format(min_index)


def order_search(target, items):
    """
    顺序搜索，常用遍历方法, O(n)
    :param target:
    :param items:
    :return:
    """
    position = 0
    while position < len(items):
        if target == items[position]:
            return position
        position += 1
    return '404 Not FOUND!:('


def binary_search(target, items):
    """
    二分查找（二叉搜索），O(log2n)
    前置条件：列表已排好序
    :param target:
    :param items:
    :return:
    """
    left = 0
    right = len(items) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == items[middle]:
            return 'where index: {}'.format(middle)
        elif target > items[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == '__main__':
    items1 = [1, 3, 6, 23, 0]
    min_search_res = min_search(items1)
    print(min_search_res)

    items2 = [1, 3, 6, 23, 66]
    min_search_res = binary_search(66, items2)
    print(min_search_res)

