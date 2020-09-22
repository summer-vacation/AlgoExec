# -*- coding: utf-8 -*-
"""
File Name:    is_palindrome_list.py
Author :      jynnezhang
Date:         2020/9/22 12:10 上午
Description:
回文链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head) -> bool:
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val
        fast = slow = q = head
        while fast.next and fast.next.next:  # 这里快指针的判读条件跟判断环形有一点不同
            fast = fast.next.next
            slow = slow.next

        def reverse_list(head):
            if head is None:
                return head
            cur = head
            pre = None
            nxt = cur.next
            while nxt:
                cur.next = pre
                pre = cur
                cur = nxt
                nxt = nxt.next
            cur.next = pre
            return cur

        p = reverse_list(slow.next)
        while p.next:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return p.val == q.val
