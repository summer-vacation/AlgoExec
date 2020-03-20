# -*- coding: utf-8 -*-
"""

   File Name：     hasCycle
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/916/
"""
from tencent.linkedlist.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        fast = head
        slow = head

        while True:
            if fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            else:
                return False
            if slow == fast:
                return True


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    print(Solution().hasCycle(root))
