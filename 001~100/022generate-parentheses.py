#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

参考链接：
https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation
"""


class Solution2:
    def generateParenthesis(self, n: int) -> list:
        if not n:
            return []
        left, right, ans = n, n, []
        self.helper(left, right, '', ans)
        return ans

    def helper(self, left, right, item, res):
        if left:
            self.helper(left-1, right, item+'(', res)
        if right > left:
            self.helper(left, right-1, item+')', res)
        if not left and not right:
            res.append(item)
            return


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]


if __name__ == '__main__':
    integer = 3
    result = Solution().generateParenthesis(integer)
    print(result)





