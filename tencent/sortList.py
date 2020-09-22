# -*- coding: utf-8 -*-
"""

   File Name：     sortList
   Author :       jing
   Date：          2020/3/31
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        left, right = self.sortList(head), self.sortList(slow)
        return self.merge(left, right)

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            head = ListNode(l1.val)
            head.next = self.merge(l1.next, l2)
        else:
            head = ListNode(l2.val)
            head.next = self.merge(l1, l2.next)
        return head
