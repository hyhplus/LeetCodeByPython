#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
19. 给定链表，从链表末尾删除第n个节点并返回其头部
"""


class Solution:
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions
    def removeNthFromEnd(self, head_, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head_)[1]

