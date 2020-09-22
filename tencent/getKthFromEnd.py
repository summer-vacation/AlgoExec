# -*- coding: utf-8 -*-
"""

   File Name：     getKthFromEnd
   Author :       jing
   Date：          2020/3/24

   链表的倒数第k个结点
"""

from tencent.linkedlist.ListNode import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return None
        fast = head
        slow = head
        for i in range(k):
            if fast:
                fast = fast.next
            else:
                return None     # 长度 < k
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    print(Solution().getKthFromEnd(head, 2))
