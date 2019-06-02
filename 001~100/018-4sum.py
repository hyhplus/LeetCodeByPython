#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Given an array nums of n integers and an integer targets,
are there elements a, b, c, and d in nums such that a + b + c + d = targets?
Find all unique quadruplets in the array which gives the sum of targets.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and targets = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]"""
"""
参考思路：

https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
核心是实现一个快速的2指针来解决2和，以及递归以将N和减少到2和.
知道列表已排序，进行了一些优化.
传递指针，而不是切片列表.
"""


class Solution(object):
    def fourSum(self, nums, target):
        def findNsum(ls, r, targets, N, result, results):
            if r-ls+1 < N or N < 2 or targets < nums[ls]*N or targets > nums[r]*N:   # early termination <提前终止>
                return

            if N == 2:   # two pointers solve sorted 2-sum problem <双指针解决2数之和>
                while ls < r:
                    s = nums[ls] + nums[r]
                    if s == targets:
                        results.append(result + [nums[ls], nums[r]])
                        ls += 1
                        while ls < r and nums[ls] == nums[ls-1]:
                            ls += 1
                    elif s < targets:
                        ls += 1
                    else:
                        r -= 1

            else:   # recursively reduce N <递归减少N>
                for i in range(ls, r+1):
                    if i == ls or (i > ls and nums[i-1] != nums[i]):
                        findNsum(i+1, r, targets-nums[i], N-1, result+[nums[i]], results)
        nums.sort()
        result_list = []
        findNsum(0, len(nums)-1, target, 4, [], result_list)
        
        return result_list


if __name__ == '__main__':
    rst_list = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    print(rst_list)

