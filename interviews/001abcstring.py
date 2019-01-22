#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给你一个字符串，比如“abc”，请打印出该字符串的所有排列组合，
如abc: abc,acb,bac,bca,cab,cba, 实际的字符长度超过100个字符串。
"""


class Solution:

    def all_string_play(self, s):
        """
        :param s: str
        :return str_list: list
        """
        if len(s) <= 1:
            return [s]
        else:
            str_list = []
            for i in range(len(s)):
                for j in self.all_string_play(s[0:i]+s[i+1:]):
                    str_list.append(s[i] + j)
                    print(str_list)
            return str_list


if __name__ == '__main__':
    string = 'my_'
    result = Solution().all_string_play(string)
    print(result)


# def fun1(s):
#     if len(s) <= 1:
#         return [s]
#     else:
#         sl = []
#         for i in range(len(s)):
#             for j in fun1(s[0:i] + s[i + 1:]):
#                 sl.append(s[i] + j)
#         return sl
# 
# 
# def main():
#     a = fun1('abc')
#     print(a)
# 
# 
# if __name__ == '__main__':
#     main()
