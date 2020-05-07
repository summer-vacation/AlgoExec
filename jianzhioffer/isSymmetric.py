# -*- coding: utf-8 -*-
"""
File Name:    isSymmetric.py
Author :      jynnezhang
Date:         2020/4/30 11:42 上午
Description:

https://leetcode-cn.com/problems/symmetric-tree/
https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
对称的二叉树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.recur(root.left, root.right)

    def recur(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.recur(left.left, right.right) and self.recur(left.right, right.left)
