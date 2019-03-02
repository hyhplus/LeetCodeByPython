#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3Sum 三数之和
eg: -1+0+1=0

"""


class Solution:

    def threeSum(self, nums):
        """
        @param nums: list[int]
        @return: List[List[int]]
        """
        d = {}
        for val in nums:
            d[val] = d.get(val, 0) + 1

        pos = [x for x in d if x > 0]
        neg = [x for x in d if x < 0]

        res = []
        if d.get(0, 0) > 2:
            res.append([0, 0, 0])

        for x in pos:
            for y in neg:
                s = -(x + y)
                if s in d:
                    if s == x and d[x] > 1:
                        res.append([x, x, y])
                    elif s == y and d[y] > 1:
                        res.append([x, y, y])
                    elif y < s < x:
                        res.append([x, y, s])
        return res


if __name__ == '__main__':
    sl_1 = [-1, 0, 1, -2, 2, -3, 3]
    result = Solution().threeSum(sl_1)
    print(result)



