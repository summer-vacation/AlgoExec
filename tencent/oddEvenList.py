# -*- coding: utf-8 -*-
"""

   File Name：     oddEvenList
   Author :       jing
   Date：          2020/4/7

   https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/31/linked-list/83/
   奇偶链表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return head

        even = head.next
        odd = head.next.next
        head.next = odd
        tail = even
        while odd.next:
            even.next = even.next.next
            even = even.next
            odd.next = odd.next.next
            if odd.next:
                odd = odd.next
        odd.next = tail
        even.next = None

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().oddEvenList(head))
