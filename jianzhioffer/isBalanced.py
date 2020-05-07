# -*- coding: utf-8 -*-
"""
File Name:    isBalanced.py
Author :      jynnezhang
Date:         2020/5/1 12:47 下午
Description:

判断平衡二叉树


https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
https://leetcode-cn.com/problems/balanced-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 此方法会有很对重复的计算，，费时
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        #  重要！！！
        if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    # 遍历时剪枝
    def isBalanced2(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
