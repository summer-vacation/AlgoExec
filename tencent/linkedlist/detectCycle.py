# -*- coding: utf-8 -*-
"""

   File Name：     detectCycle
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/917/

   返回入环的节点的index
"""
from tencent.linkedlist.ListNode import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        hasCycle = False
        fast = head
        slow = head
        while True:
            if fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            else:
                hasCycle = False
                break
            if slow == fast:
                hasCycle = True
                break

        # 步骤二：若有环，找到入环开始的节点
        # 链表头到环入口的距离=相遇点到环入口的距离+（n-1）圈环长度
        if hasCycle:
            cur = head
            while slow != cur:
                cur = cur.next
                slow = slow.next
            return slow
        else:
            return None
