# -*- coding: utf-8 -*-
"""

   File Name：     mergeTwoLists
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/910/
"""

from tencent.linkedlist.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        self.merge(l1, l2, result)
        return result.next

    def merge(self, l1, l2, result):
        if l1 is None and l2 is None:
            return
        elif l1 is not None and l2 is None:
            result.next = l1
            return
        elif l1 is None and l2 is not None:
            result.next = l2
            return
        else:
            if l1.val <= l2.val:
                result.next = l1
                self.merge(l1.next, l2, result.next)
            else:
                result.next = l2
                self.merge(l1, l2.next, result.next)

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0)
        cur=head
        cur1=l1
        cur2=l2
        while cur1 and cur2:
            if cur1.val<=cur2.val:
                cur.next=cur1
                cur1=cur1.next
            else:
                cur.next=cur2
                cur2=cur2.next
            cur=cur.next
        if cur1:
            cur.next=cur1
        if cur2:
            cur.next=cur2
        return head.next

    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next , l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next , l1)
            return l2


if __name__ == '__main__':
    print(Solution().mergeTwoLists())
