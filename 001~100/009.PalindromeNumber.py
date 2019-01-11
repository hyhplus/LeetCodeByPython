#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
确定整数是否是回文。当它向前读取向后时，整数是回文。

例1：
输入： 121
输出： true

例2：
输入： -121
输出： false
说明：从左到右，它读取-121。从右到左，它变成121-。因此它不是回文。

Follow up:
Could you solve it without converting the integer to a string?
"""
from timeDecorator import clock


@clock
class Solution:
    def isPalindrome(self, x):
        """
        解法一（官方不推荐）：将`int`转为`str`
        : type x: int
        : rtype: bool
        """
        return str(x) == str(x)[::-1]


@clock
class Solution2:
    def isPalindrome(self, x):
        """
        解法二： 循环整个整型数字进行截取回文串
        : type x: int
        : rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            reverse_num = 0
            while x > reverse_num:                                  # 循环整个整型数字
                reverse_num = reverse_num * 10 + x % 10             # 得到回文左侧（或右侧）一边的值
                x //= 10                                            # 循环一次，整除一次10
                print(reverse_num)
                print(x)

            return (x == reverse_num) or (x == reverse_num//10)     # 奇数偶数问题，奇数要多整除10


if __name__ == '__main__':
    integer = 1221
    result = Solution().isPalindrome(integer)
    print(result)

    result2 = Solution2().isPalindrome(integer)
    print(result2)
