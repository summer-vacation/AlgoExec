# -*- coding: utf-8 -*-
"""

   File Name：     maxDepth
   Author :       jing
   Date：          2020/4/13

   二叉树的深度

   https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
