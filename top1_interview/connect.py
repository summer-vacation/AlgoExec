# -*- coding: utf-8 -*-
"""
File Name:    connect.py
Author :      jynnezhang
Date:         2020/9/28 1:20 下午
Description:

填充每个节点的下一个右侧节点指针 II
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> None:
        if root is None:
            return root
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                if i < size - 1:
                    cur.next = queue[0]
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    Solution().connect(root)
