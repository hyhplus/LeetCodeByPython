#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个整数数组，返回两个数字的索引，使它们相加到特定目标。
可以假设每个输入只有一个解决方案，并且可能不会两次使用相同的元素。

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        算法思路：
            新建一个字典，字典的key: 列表的元素（值）; 字典的value: 列表的值的索引。
            遍历这个列表的时候，获取字典的key存在：target-nums[x]的时候，则返回此索引和当前索引。
        :param nums:
        :param target:
        :return:
        """
        new_dic = dict()
        for x in range(len(nums)):
            sec = new_dic.get(target - nums[x], -1)  # dict.get(key): key是要的值，不存在则返回-1
            print(sec)
            if sec >= 0:
                return [sec, x], new_dic
            else:
                new_dic[nums[x]] = x


a = Solution()
b = a.twoSum([3, 11, 0, 1, 7, 8, 1, 7], 9)
print(b)

