#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """ 
        方法一：暴力法，可运行。但是提交超时，不可通过。
        """
        # max_ = 0
        # for i in range(len(height)):
        #
        #     for j in range(i+1, len(height)):
        #         max_ = max(max_, min(height[i], height[j]) * (j - i))
        #
        # return max_

        # # 双指针法解1
        # res, l, r = 0, 0, len(height)-1
        # while l < r:
        #     h = min(height[l], height[r])
        #     res, l, r = max(res, h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        # return res

        # # 双指针法解2
        # max_area = 0,
        # left = 0,
        # right = len(height) - left,
        #
        # while left < right:
        #     max_area = max(max_area, min(height[left], height[right]) * (right - 1))
        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return max_area

        """
        方法二：双指针法(3)，分别从列表左右两端遍历（while），面积=短边*距离，哪边短遍历时+1，因为短的已达最大值。
        """
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            width = j - i
            length = min(height[i], height[j])
            volume = width * length
            if max_area < volume:
                max_area = volume
            if length == height[i]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == '__main__':
    integer_list = [1, 3, 3, 9, 12, 1, 2, 43, 2, 23, 2, 2, 23, 23, 23, 2]
    result = Solution().maxArea(integer_list)
    print(result)
