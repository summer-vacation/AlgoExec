# -*- coding: utf-8 -*-
"""
File Name:    getIntersectionNode.py
Author :      jynnezhang
Date:         2020/5/5 1:54 下午
Description:

两个链表的第一个公共节点
https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB) -> ListNode:
        if headA is None or headB is None:
            return None
        lensA, lensB = 0, 0
        preA, preB = headA, headB
        while preA:
            lensA += 1
            preA = preA.next
        while preB:
            lensB += 1
            preB = preB.next
        if lensA < lensB:
            headA, headB = headB, headA
            more = lensB - lensA
        else:
            more = lensA - lensB
        while more and headA:
            headA = headA.next
            more -= 1
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headB = headB.next
                headA = headA.next
        return 0


# listA = [4,1,8,4,5], listB = [5,0,1,8,4,5],
listA = ListNode(4)
listA.next = ListNode(1)
listA.next.next = ListNode(8)
listA.next.next.next = ListNode(4)

listB = ListNode(5)
listB.next = ListNode(0)
listB.next.next = ListNode(1)
listB.next.next.next = listA.next.next

print(Solution().getIntersectionNode(listA, listB))
