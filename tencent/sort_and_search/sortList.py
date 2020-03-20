# -*- coding: utf-8 -*-
"""

   File Name：     sortList
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/932/
"""

from tencent.linkedlist.ListNode import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        result.sort()
        root = head
        for n in result:
            root.next = ListNode(n)
            root = root.next
        return head

