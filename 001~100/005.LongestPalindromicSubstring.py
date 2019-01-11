#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个字符串s，找出s中最长的回文子字符串。可以假设s的最大长度为1000。

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        这是这个出色的C ++解决方案的Python版本。
        while k < lenS - 1 and s[k] == s[k + 1]: k += 1是非常有效的，
        可以处理odd-length（abbba）和even-length（abbbba）。
        """
        len_s = len(s)
        if len_s <= 1: 
            return s
        min_start, max_len, i = 0, 1, 0
        while i < len_s:
            if len_s - i <= max_len/2: 
                break
            j, k = i, i
            while k < len_s-1 and s[k] == s[k+1]:
                k += 1
            i = k + 1
            while k < len_s-1 and j and s[k+1] == s[j-1]:
                k, j = k+1, j-1
            if k-j+1 > max_len:
                min_start, max_len = j, k-j+1
        return s[min_start: min_start + max_len]
    
        
if __name__ == '__main__':
    string = 'test sub aba '
    result = Solution().longestPalindrome(string)
    print(result)







