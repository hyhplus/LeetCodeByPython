#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

大小分别为m和n的已排序数组nums1和nums2。
找到两个排序数组的中值。总体运行时复杂性应为O（log（m+n））。
你可以假定nums1和nums2不能同时为空。

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, x, y):
        z = len(x) + len(y)
        return self.findKth(x, y, z//2) if z % 2 == 1 \
            else (self.findKth(x, y, z//2-1)+self.findKth(x, y, z//2))/2.0

    def findKth(self, list1, list2, k):
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        if not list1:
            return list2[k]
        if k == len(list1) + len(list2) - 1:
            return max(list1[-1], list2[-1])
        i = len(list1) // 2
        j = k - i
        if list1[i] > list2[j]:
            # Here it's O(1) to get list1[:i] and list2[j:].
            return self.findKth(list1[:i], list2[j:], i)
        else:
            return self.findKth(list1[i:], list2[:j], j)


if __name__ == '__main__':
    nums1 = (1, 2, 4, 9)
    nums2 = (1, 2, 4, 8)
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)
