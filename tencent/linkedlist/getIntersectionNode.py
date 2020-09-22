# -*- coding: utf-8 -*-
"""

   File Name：     getIntersectionNode
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/918/

   链表相交
"""

from tencent.linkedlist.ListNode import ListNode

"""
    先计算长度
    
    长的链表先走，走到剩余长度一样时，再一起走，有相同就说明相交
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        lenA, lenB = 0, 0
        a, b = headA, headB
        while a.next is not None:
            a = a.next
            lenA += 1
        while b.next is not None:
            b = b.next
            lenB += 1
        if lenA > lenB:
            step, a, b = lenA - lenB, headA, headB
        else:
            step, a, b = lenB - lenA, headB, headA

        while step:
            step -= 1
            a = a.next

        while a != b:
            a, b = a.next, b.next
        return a
