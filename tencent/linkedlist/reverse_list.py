# -*- coding: utf-8 -*-
"""

   File Name：     reverse_list
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/920/
"""

from tencent.linkedlist.ListNode import ListNode


class Solution:
    def reverseList_re(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        r = self.reverseList_re(head.next)
        head.next.next = head
        head.next = None
        return r

    # 构造一个None，然后将所有的node移到
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        pre = None
        cur = head
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    print(Solution().reverseList(root))
