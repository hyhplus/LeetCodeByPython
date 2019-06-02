#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = '( )'

len_ = len(s.split())
s = (s.split())

if len_ % 2 != 0:
    print(False)

left_l = ['(', '{', '[']
right_l = [')', '}', ']']
for i_ in range(len_):
    pass


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 堆栈以跟踪开放的括号
        stack = []

        # 用于跟踪映射的哈希映射，这使代码非常简洁
        # 还可以更轻松地添加更多类型的括号
        mapping = {")": "(", "}": "{", "]": "["}

        # 对于表达式中的每个括号
        for char in s:

            # 如果该字符是结束括号
            if char in mapping:

                # 如果非空，则弹出堆栈中最顶层的元素
                # 否则为top_element变量指定一个虚拟值‘#’
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


class Solution2:
    def isValid(self, s: 'str') -> 'bool':
        v = []
        d = {']': '[', ')': '(', '}': '{'}
        for i in range(len(s)):
            if s[i] in d.values():
                v.append(s[i])
            elif s[i] in d.keys():
                if len(v) == 0:
                    return False
                elif v[-1] == d[s[i]]:
                    v.pop()
                else:
                    return False
        if v is []:
            return True
        else:
            return False
