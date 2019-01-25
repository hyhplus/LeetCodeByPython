#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
14、最长公共前缀
"""


# class Solution:
#     def longestCommonPrefix(self, sl):
#         """
#         :type sl: List[str]
#         :rtype: str
#         """
#         if '' in sl:
#             return ''
#         n = len(sl)
#         if n > 1:
#             pr = ''
#             for index, st in enumerate(sl[0]):
#                 pr += st
#                 for j in range(1, n):
#                     if pr not in sl[j][:index+1]:
#                         break
#                 else:
#                     continue
#                 break
#             else:
#                 return pr
#             return pr[:-1]
#         else:
#             return '' if not n else sl[0]


# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         common = None
#         for s in strs:
#             if common is None:
#                 common = list(s)
#             else:
#                 for i, c in enumerate(common):
#                     if i >= len(s) or c != s[i]:
#                         common = common[:i]
#                         break
#         return ''.join(common) if common else ''


# class Solution:
#     def longestCommonPrefix(self, m):
#         if not m:
#             return ''
#         s1 = min(m)
#         print(s1)
#         s2 = max(m)
#         print(s2)
#
#         for i, c in enumerate(s1):
#             if c != s2[i]:
#                 return s1[:i]  # stop until hit the split index
#         return s1


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


if __name__ == '__main__':
    sl_1 = ['flow', 'fawer', 'flower']
    result = Solution().longestCommonPrefix(sl_1)
    print(result)


