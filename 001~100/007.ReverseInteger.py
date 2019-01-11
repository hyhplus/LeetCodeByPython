#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7. Reverse Integer
给定32位有符号整数，整数的反向数字。

例1：
输入： 123
输出： 321

例2：
输入： -123
输出： -321

例3：
输入： 120
输出： 21
"""
from timeDecorator import clock


@clock
class Solution:
    def reverse(self, x):
        """
        : type x: int
        : rtype: int
        """
        if x < 0:
            number = int("-" + str(abs(x))[::-1])  # [::-1]表示反转字符串
        else:
            number = int(str(abs(x))[::-1])

        if number > (2 ** 31 - 1) or number < -(2 ** 31):   # 溢出返回0
            return 0
        return number


class Solution2:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = lambda x: x and (1, -1)[x < 0]
        r = int(str(sign(x)*x)[::-1])
        return (sign(x)*r, 0)[r > 2**31 - 1]


@clock
class Solution3(object):
    def reverse(self, x):
        s = (x > 0) - (x < 0)
        print(s)
        r = int(str(x*s)[::-1])
        return s*r * (r < 2**31)


@clock
class Solution4:
    def reverse(self, x):
        sign = -1 if x <= 0 else 1
        ans = int(str(sign*x)[::-1])
        return ans*sign if ans < 2**31 else 0


if __name__ == '__main__':
    num = -120
    result = Solution4().reverse(num)
    print(result)
