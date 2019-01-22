#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
12. 整型转为罗马数字
"""


class Solution:
    def intToRoman(self, num):
        """
        解法一：通过枚举+遍历列表的限制
        :type num: int
        :rtype: str
        """
        stl = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        ret = ""

        for i, j in enumerate(nums):
            while num >= j:
                ret += stl[i]
                num -= j
            if num == 0:
                return ret


class Solution2:
    def intToRoman(self, num):
        """
        解法二：数据库存储方法(列表索引对应0-9)，相当于从数据库取值
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        # or return M[num//1000] + C[(num//100) % 10] + X[(num//10) % 10] + I[num % 10]
        return M[num//1000] + C[(num % 1000)//100] + X[(num % 100)//10] + I[num % 10]


if __name__ == '__main__':
    integer = 1775
    result = Solution().intToRoman(integer)
    print(result)
    result2 = Solution2().intToRoman(integer)
    print(result2)

    a = 4321
    print((a % 10)//10)
    print(a % 100)

    # print((a // 10) % 10)
    # print((a // 100) % 10)
    # print(a // 1000)

