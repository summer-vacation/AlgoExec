# -*- coding: utf-8 -*-
"""

   File Name：     removeElements
   Author :       jing
   Date：          2020/3/24

   https://leetcode-cn.com/problems/remove-linked-list-elements/

   移除链表元素
"""
from tencent.linkedlist.ListNode import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None

        cur = ListNode(0)
        cur.next = head
        res = cur
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return res.next


if __name__ == '__main__':
    root = ListNode(6)
    root.next = ListNode(2)
    root.next.next = ListNode(6)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    root.next.next.next.next.next = ListNode(6)
    print(Solution().removeElements(root, 6))
