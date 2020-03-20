# -*- coding: utf-8 -*-
"""

   File Name：     deleteNode
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/919/
   删除链表中的节点
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        删除node
        """
        node.val = node.next.val
        node.next = node.next.next
