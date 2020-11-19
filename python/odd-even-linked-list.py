# -*- coding: utf-8 -*-
"""
File Name:    odd-even-linked-list.py
Author :      jynnezhang
Date:         2020/11/13 2:37 下午
Description:
"""
from tencent.sortList import ListNode


class Solution:
    def oddEvenList(self, head):
        if not head.next or not head.next.next:
            return head
        odd = head
        even = head.next
        even_list = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_list
        return head


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    root.next.next.next.next.next = ListNode(6)
    Solution().oddEvenList(root)

