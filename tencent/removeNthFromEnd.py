# -*- coding: utf-8 -*-
"""

   File Name：     removeNthFromEnd
   Author :       jing
   Date：          2020/3/24
"""

from tencent.linkedlist.ListNode import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        res = ListNode(0)
        res.next = head
        l1 = res
        l2 = res
        for i in range(n):
            l1 = l1.next
        while l1.next:
            l1 = l1.next
            l2 = l2.next
        l2.next = l2.next.next
        return res.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().removeNthFromEnd(head, 2))
