#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
17

Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.

2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
"""


class Solution:
    def letterCombinations(self, digits):
        """

        :param digits: str
        :return: List[str]
        """
        # Edge-case
        if not digits:
            return []

        import itertools
        # Create dictionary of lists representing each number
        num_dict = dict()
        num_dict['0'] = []
        num_dict['1'] = []
        num_dict['1'] = []
        num_dict['2'] = ['a', 'b', 'c']
        num_dict['3'] = ['d', 'e', 'f']
        num_dict['4'] = ['g', 'h', 'i']
        num_dict['5'] = ['j', 'k', 'l']
        num_dict['6'] = ['m', 'n', 'o']
        num_dict['7'] = ['p', 'q', 'r', 's']
        num_dict['8'] = ['t', 'u', 'v']
        num_dict['9'] = ['w', 'x', 'y', 'z']

        num_list = [num_dict[c] for c in digits]
        soln_list = []
        for r in itertools.product(*num_list):
            soln_list.append(''.join(r))
        return soln_list


if __name__ == '__main__':
    sl_1 = '345'
    result = Solution().letterCombinations(sl_1)
    print(result)
