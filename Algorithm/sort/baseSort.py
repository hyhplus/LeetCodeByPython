#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
排序算法：

O（n^2）
冒泡排序
插入排序
选择排序

Q(n log n) 分而治之
快速排序
归并排序
"""


def bubble(sl):
    """
    冒泡排序，O(n^2)
    相邻的两个元素对比，大的后推，遍历整个列表一次后，将最大项以冒泡的方式排列到列表末尾
    :param sl: list
    :return:
    """
    for i in range(len(sl)-1):
        for j in range(i+1, len(sl)):
            if sl[i] > sl[j]:
                sl[i], sl[j] = sl[j], sl[i]
    return sl


def bubble_sorted(items):
    """
    优化的冒泡排序，
    最好 O(n),
    最坏 O(n^2)
    平均 O(n^2)
    """
    n = len(items)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if items[i] < items[i-1]:
                items[i], items[i-1] = items[i-1], items[i]
                swapped = True
            i += 1
        if not swapped:
            return items
        n -= 1


def bubble_sort(items):
    """
    冒泡排序, 还是while循环换为for循环比较习惯
    最好 O(n)
    最坏 O(n^2)
    """
    items_len = len(items)
    for i in range(1, items_len):
        has_swap = False
        for j in range(1, items_len):
            if items[j - 1] > items[j]:
                has_swap = True
                items[j - 1], items[j] = items[j], items[j - 1]
        if not has_swap:
            break
    return items


def select_sort(items):
    """
    选择排序, 搜索整个列表，找到最小项位置
    """
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        if min_index != i:
            items[min_index], items[i] = items[i], items[min_index]

    return items


def insert_sort(items):
    """
    插入排序
    从第二个数开始找前面对应顺序的位置，像插入一张扑克牌顺序一样排好序
    :param items: list
    :return:
    """
    i = 1
    while i < len(items):
        item_insert = items[i]
        j = i - 1
        while j >= 0:
            if item_insert < items[j]:
                items[j+1] = items[j]
                j -= 1
            else:
                break
        items[j+1] = item_insert
        i += 1
    return items


def insert_sort_for(items):
    """
    插入排序，for循环, 中间还是while容易理解：
    比插入的值 大的数挪后，直到不需要挪动为止即为插入的位置。
    :param items:
    :return:
    """
    for i in range(1, len(items)):
        item_insert = items[i]
        j = i - 1
        while j >= 0:
            if item_insert < items[j]:
                items[j + 1] = items[j]     # 比插入值大的元素，向后移动一位
                j -= 1
            else:                           # 不需要挪动时，跳出循环
                break
        items[j + 1] = item_insert          # 找到了插入的位置

    return items


if __name__ == '__main__':
    my_sl = [1, 3, 23, 21, 12, 22, 234]
    result1 = bubble(my_sl)
    print(result1)

    result2 = bubble_sorted(my_sl)
    print(result2)

    result3 = select_sort(my_sl)
    print(result3)

    my_s2 = [1, 3, 23, 21, 12, 22, 234]
    result5 = insert_sort_for(my_s2)
    print(result5)


