# -*- coding: utf-8 -*-
"""

   File Name：     middleNode
   Author :       jing
   Date：          2020/3/23

   https://leetcode-cn.com/problems/middle-of-the-linked-list/

   链表的中间结点
"""
from tencent.linkedlist.ListNode import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            return slow.next        # 偶数，选第二个
        else:
            return slow

    def middleNode2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.val


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    print(Solution().middleNode2(head))


