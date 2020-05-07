# -*- coding: utf-8 -*-
"""
File Name:    mirrorTree.py
Author :      jynnezhang
Date:         2020/4/28 5:32 下午
Description:

二叉树的镜像
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.dfs(root)
        return root

    def dfs(self, cur):
        if cur is None:
            return
        self.dfs(cur.left)
        self.dfs(cur.right)
        left = cur.left
        right = cur.right
        cur.left, cur.right = right, left


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
Solution().mirrorTree(root)
