#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


您将获得两个非空链表，表示两个非负整数。数字以相反的顺序存储，每个节点包含一个数字。
添加两个数字并将其作为链接列表返回。
您可以假设这两个数字不包含任何前导零，除了数字0本身。

例：
输入：（2  - > 4  - > 3）+（5  - > 6  - > 4）
 输出： 7  - > 0  - > 8
 说明： 342 + 465 = 807。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """

        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        carry = 0
        head = node = ListNode('#')
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, rem = divmod(carry + val1 + val2, 10)
            node.next = ListNode(rem)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:   # 进一位
            node.next = ListNode(carry)

        return head.next


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(9)
    result = Solution().addTwoNumbers(a, b)
    assert '{0}->{1}->{2}->{3}'.format(result.val, result.next.val, result.next.next.val, result.next.next.next.val) \
           == '7->0->3->1'   # assert 断言：判断结果是否正确；不正确则程序异常

    print(result.val, result.next.val, result.next.next.val, result.next.next.next.val)




