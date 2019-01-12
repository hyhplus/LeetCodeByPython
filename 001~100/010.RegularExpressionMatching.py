#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
10. 正则表达式匹配
hard

给定输入字符串和模式（P），实现与“.”和“*”支持匹配的正则表达式。
“.”匹配任何单个字符。
“*”与前面的单个元素零个或多个匹配。
匹配应该覆盖整个输入字符串（而不是部分）。

注：
s可以为空，并且只包含小写字母a-z。
p可以为空，只包含小写字母a-z和类似的字符。或者*。

例1：
输入：S＝“AA”, P=“A”
输出：假
说明：“a”与整个字符串“a a”不匹配。

例2：
输入：S＝“AA”, P=“a*”
输出：真
解释：“*”表示前面元素“a”的零个或多个。因此，重复“a”一次，它就变成“aa”。

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
"""
from timeDecorator import clock


@clock
class Solution:
    def isMatch(self, s, p):
        """ s:str, p:str"""
        def dfs(s_idx, p_idx, memo):
            if (s_idx, p_idx) in memo:
                return memo[(s_idx, p_idx)]

            if p_idx >= len(p):
                return s_idx == len(s)

            cur_match = s_idx < len(s) and (
                s[s_idx] == p[p_idx] or p[p_idx] == "."
            )

            if p_idx + 1 < len(p) and p[p_idx+1] == "*":
                match = dfs(s_idx, p_idx+2, memo) or \
                        (cur_match and dfs(s_idx+1, p_idx, memo))

            else:
                match = cur_match and dfs(s_idx+1, p_idx+1, memo)

            memo[(s_idx, p_idx)] = match

            return match
        return dfs(0, 0, {})


if __name__ == '__main__':
    str1 = '123321312s'
    p1 = '123.*s'

    result = Solution().isMatch(str1, p1)
    print(result)

    # result2 = Solution2().isMatch(str1, p1)
    # print(result2)




