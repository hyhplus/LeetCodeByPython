#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个字符串，在不重复字符的情况下查找最长子字符串的长度。

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        算法思路：遍历字符串，获取最长子串的首尾索引即可
        :param s: str
        :return: int
        """
        idx, n, start, res = [0] * 128, len(s), 0, 0
        for i in range(n):
            start = max(start, idx[ord(s[i])])     # 子串起始索引
            res = max(res, i - start + 1)          # 子串长度
            idx[ord(s[i])] = i + 1
        return res


if __name__ == '__main__':
    _s = 'Longest Substring Without Repeating Characters'
    s = 'test my string.'
    result = Solution().lengthOfLongestSubstring(s)
    print(result)


