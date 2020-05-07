# -*- coding: utf-8 -*-
"""

   File Name：     copyRandomList
   Author :       jing
   Date：          2020/4/13

    复杂链表的复制
   https://leetcode-cn.com/problems/copy-list-with-random-pointer/
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        # Generate New Nodes after Old Nodes
        point = head
        while point:
            new_node = Node(point.val)
            new_node.next = point.next  # Link back
            point.next = new_node       # Link front

            point = new_node.next

        # Modify new_node.random
        point = head
        while point:
            next_node = point.next.next  # Store the pointer of next node group
            point.next.next = next_node.next if next_node else None  # NEXT pointer
            point.next.random = point.random.next if point.random else None # RANDOM pointer

            point = next_node

        return head.next
