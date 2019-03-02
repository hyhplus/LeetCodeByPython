#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
16. 最接近的三数之和

eg:
target=3， list=[1,2,3,1]
最接近的值：1+1+2=4，返回整型数值：4
"""


class Solution:
    def three_sum_closest(self, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: res's type is int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            ls, r = i+1, len(nums)-1
            while ls < r:
                s = sum((nums[i], nums[ls], nums[r]))
                if abs(s-target) < abs(res-target):
                    res = s
                if s < target:
                    ls += 1
                elif s > target:
                    r -= 1
                else:
                    return res
        return res


class Solution2:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        nums.sort()
        # result = nums[0]+nums[1]+nums[2]
        close = []
        for i in range(0, nums.__len__()-2):
            j, k = i+1, nums.__len__()-1
            if nums[i]+nums[k-1]+nums[k] < target:
                close.append(nums[i]+nums[k-1]+nums[k])
            elif nums[i]+nums[j]+nums[j+1] > target:
                close.append(nums[i]+nums[j]+nums[j+1])
            else:
                while j < k:
                    temp = nums[i]+nums[j]+nums[k]
                    if temp == target:
                        return temp
                    close.append(temp)
                    if temp < target:
                        j += 1
                    else:
                        k -= 1
        closest = sorted(close, key=lambda x: abs(target-x))
        return closest[0]


if __name__ == '__main__':
    sl_1 = [-1, 3, 3, 2, 1]
    result = Solution().three_sum_closest(sl_1, 3)
    print(result)
    result2 = Solution2().threeSumClosest(sl_1, 3)
    print(result2)




