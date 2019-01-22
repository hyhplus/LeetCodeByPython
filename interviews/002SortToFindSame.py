#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
两个排好序的数组（从小到大）找出重复的元素，例如：
数组A: [1,2,3,4]
数组B: [2,4,5,6]
输出: [2,4]

"""
from timeDecorator import clock


class Solution:
    @clock
    def sort_find_same(self, list_a, list_b):
        """
        解法一：暴力法, O(n^2)
        :param list_a: list
        :param list_b: list
        :return list_same: list
        """
        list_same = []
        for i in range(len(list_a)):
            for j in range(len(list_b)):
                if list_a[i] == list_b[j]:
                    list_same.append(list_a[i])
        return list_same

    @clock
    def sort_common(self, list_a, list_b):
        """
        解法二：归并排序，遍历一次两个列表中的最大长度，通过指针递增获取相同元素并保存到common_list中
        归并排序是对几个有序表有序表的排序，合并成一个新的有序表
        https://blog.csdn.net/RedSun528/article/details/82930117
        https://blog.csdn.net/csdn_564174144/article/details/77150346
        :param list_a:
        :param list_b:
        :return: common_list
        """
        common_list, a, b = list(), 0, 0
        max_len = max(len(list_a), len(list_b))
        for i in range(max_len):
            if list_a[a] > list_b[b]:
                b += 1
            elif list_a[a] < list_b[b]:
                a += 1
            elif list_a[a] == list_b[b]:
                common_list.append(list_a[a])
                a += 1
                b += 1

        return common_list


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15, 16, 17, 18, 19,
             20, 21, 22, 23, 24, 25, 26, 27, 28, 112, 123, 124, 1256, 1344, 12345, 23456]
    list2 = [2, 4, 6, 12, 14, 16, 122, 1234, 12223, 124144]

    result = Solution().sort_find_same(list1, list2)
    print(result)

    result2 = Solution().sort_common(list1, list2)
    print(result2)




