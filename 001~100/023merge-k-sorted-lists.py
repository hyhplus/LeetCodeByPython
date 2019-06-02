#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
合并k个已排序的链表并将其作为一个排序列表返回。分析并描述其复杂性。

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


"""
方法1：蛮力
算法

遍历所有链接列表并将节点的值收集到一个数组中。
对此数组进行排序和迭代，以获得正确的节点值。
创建一个新的已排序链接列表，并使用新节点对其进行扩展。

复杂性分析
时间复杂度： O（N log N）
空间复杂度： O（N）
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


"""
方法2: 分而治之
这种算法的好处是我们不需要多次遍历大多数节点

配对k个列表并合并每对。
第一次配对后，k个列表合并为k/2个列表，平均长度为2n/k，然后是k/4、k/8等。
重复此过程，直到得到最终排序的链接列表。

因此，我们将在每次配对和合并时遍历大概n个节点，并重复大概log2k时间的过程。

"""


class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next
