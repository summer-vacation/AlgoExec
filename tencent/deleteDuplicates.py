# -*- coding: utf-8 -*-
"""

   File Name：     deleteDuplicates
   Author :       jing
   Date：          2020/4/2


"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pre = dummy_head
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
                continue

            pre = pre.next
            cur = cur.next

        return dummy_head.next


head = ListNode(1)
head.next = ListNode(1)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(4)
# head.next.next.next.next.next = ListNode(4)
# head.next.next.next.next.next.next = ListNode(5)
print(Solution().deleteDuplicates(head))
