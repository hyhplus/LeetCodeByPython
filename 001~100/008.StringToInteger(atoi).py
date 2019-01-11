#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
8. 字符串转为整型
https://leetcode.com/problems/string-to-integer-atoi/

实现atoi将字符串转换为整数。
该函数首先丢弃所需数量的空白字符，直到找到第一个非空白字符。然后，从该字符开始，采用可选的初始加号或减号，后跟尽可能多的数字，并将它们解释为数值。
字符串可以包含在形成整数之后的其他字符，这些字符将被忽略并且对此函数的行为没有影响。
如果str中的第一个非空白字符序列不是有效的整数，或者由于str是空的或者只包含空白字符而不存在这样的序列，则不执行转换。
如果无法执行有效转换，则返回零值。

注意：
只有空格字符' '被视为空格字符。
假设我们正在处理一个只能在32位有符号整数范围内存储整数的环境：[ - 2^31, 2^31  - 1]。如果数值超出可表示值的范围，
则返回INT_MAX（2^31  - 1）或INT_MIN（-2^31）。

例1：
输入： “42”
输出： 42

例2：
输入： “ -  42”
输出： -42
说明：第一个非空白字符是' - '，这是减号。然后取尽可能多的数字，得到42。

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
"""
import re

from timeDecorator import clock

matcher = re.compile(r'^ *([-\+]?\d+)')


@clock
class Solution:
    def myAtoi(self, s):
        """
        Using the stupid stub that the site provided, overriding `str`
        [-<-]利用正则表达式截取字符串
        """
        match = matcher.match(s)

        if not match:
            return 0
        else:
            num = int(match.group(1))
            if num >= 0:
                return min(num, 2**31 - 1)
            elif num < 0:
                return max(num, -2**31)


@clock
class Solution2:
    def myAtoi(self, strings):
        number = ''
        meet_num = False         # 判断首字符的标志位, False
        for word in strings:
            if word == ' ' and not meet_num:
                continue
            if not word.isdigit() and word != '-' and word != '+':
                break

            if not meet_num:
                if word.isdigit() or word == '-' or word == '+':
                    number += word
                    meet_num = True         # 读取了首字符就置为True
            elif meet_num:
                if word.isdigit():          # 除了首字符可以为-，+；其余位只能是数字。
                    number += word
                else:
                    break

        if number == '' or number == '+' or number == '-':
            return 0
        elif int(number) >= 0:
            return min(int(number), 2**31 - 1)
        elif int(number) < 0:
            return max(int(number), -2**31)


if __name__ == '__main__':
    string = '234 3+2 a -12131 and string'
    result1 = Solution().myAtoi(string)
    result2 = Solution2().myAtoi(string)
    print(result1, result2)
