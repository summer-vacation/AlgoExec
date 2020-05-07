# -*- coding: utf-8 -*-
"""
File Name:    treeToDoublyList.py
Author :      jynnezhang
Date:         2020/4/28 4:02 下午
Description:

二叉搜索树与双向链表
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        if root is None:
            return None
        self.pre = None
        self.inOrder(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

    def inOrder(self, cur):
        if cur is None:
            return
        self.inOrder(cur.left)
        if self.pre:
            self.pre.right, cur.left = cur, self.pre        # 修改指向，pre.left -> cur  , cur.right ->  pre
        else:
            self.head = cur      # 头结点
        self.pre = cur      # 保存上一个结点
        self.inOrder(cur.right)


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
Solution().treeToDoublyList(root)
