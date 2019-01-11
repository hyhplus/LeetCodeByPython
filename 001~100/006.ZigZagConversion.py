#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串"PAYPALISHIRING"在给定行数上以Z字形图案写入，然后逐行阅读： "PAHNAPLSIIGYIR"
编写将采用字符串的代码并在给定多行的情况下进行此转换：
string convert（string s，int numRows）;

----

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        如果numRows是5，我们看到这样的锯齿形图案：(here Algorithmic thinking)

        我们可以看到数字0~7在这里是一个小模式，如果我们除以8，我们可以在其他小模式中获得相同的数字。如
        0％8 = 0; 8％8 = 0
        1％8 = 1; 9％8 = 1
        所以我们可以使用此功能并将它们过滤到我们存储的行中。

        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [''] * numRows
        num = (numRows-1) * 2
        for i, item in enumerate(s):
            if i % num >= numRows:
                rows[(num - i % num)] += item
            else:
                rows[i % num] += item
        return ''.join(rows)


if __name__ == '__main__':
    string = 'my path'
    row = 2
    result = Solution().convert(string, row)
    print(result)



