#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速排序的实现
时间：最好 O(n log2n) ~ 最坏 O(n^2)
空间：最好 O(log2n)   ~ 最坏 O(n)
"""


def quick_sort(items):
    quick_sort_helper(items, 0, len(items) - 1)


def quick_sort_helper(items, left, right):
    if left < right:
        pivot_location = partition(items, left, right)
        quick_sort_helper(items, left, pivot_location - 1)
        quick_sort_helper(items, pivot_location + 1, right)


def partition(items, left, right):
    middle = (left + right) // 2
    pivot = items[middle]
    items[middle] = items[right]
    items[right] = pivot

    boundary = left

    for index in range(left, right):
        if items[index] < pivot:
            items[index], items[boundary] = items[boundary], items[index]
            boundary += 1

    items[right], items[boundary] = items[boundary], items[right]

    return boundary



