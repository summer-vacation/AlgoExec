# -*- coding: utf-8 -*-
"""

   File Name：     add_two_numbers
   Author :       jing
   Date：          2020/3/16

   https://leetcode.com/problems/add-two-numbers
   链表倒求和
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        div = 0
        out = result
        # non-empty
        while l1 is not None or l2 is not None:
            if l1 and l2:
                div, mod = divmod(div + l1.val+l2.val, 10)
                l1 = l1.next
                l2 = l2.next
            elif l1 is None and l2 is not None:
                div, mod = divmod(div +l2.val, 10)
                l2 = l2.next
            elif l2 is None and l1 is not None:
                div, mod = divmod(div + l1.val, 10)
                l1 = l1.next
            result.val = mod
            if div != 0:
                result.next = ListNode(div)
            elif l1 is not None or l2 is not None:
                result.next = ListNode(0)
            result = result.next
        return out


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(8)
    # l1.next.next = ListNode(3)
    l2 = ListNode(0)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    s.addTwoNumbers(l1, l2)
