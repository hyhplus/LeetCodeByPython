#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def romanToInt(self, s):
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c

        return res


class Solution2:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res, i = 0, 0
        for i in range(len(s)):
            curr, nxt = s[i], s[i + 1:i + 2]
            print(nxt)
            if nxt and roman[curr] < roman[nxt]:
                res -= roman[curr]
            else:
                res += roman[curr]
        return res


if __name__ == '__main__':
    str1 = 'LII'
    ret = Solution2().romanToInt(str1)
    print(ret)

    list1 = [0, 1, 2, 3]
    for index in range(len(list1)):
        current, next_ = list1[index], list1[index+1:index+2]  # list1[index+1:index+2]是列表类型
        print(current, next_)

    s1 = '123'
    for index in range(len(s1)):
        current, next_ = s1[index], s1[index+1:index+2]
        print(current, next_)
        print('溢出？', s1[3:4])


