# -*- coding: utf-8 -*-
"""

   File Name：     zigzagLevelOrder
   Author :       jing
   Date：          2020/4/12

   二叉树的锯齿形层次遍历
"""
from tencent.sort_and_search.TreeNode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        levels = []

        def backtrack(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                backtrack(node.left, level + 1)
            if node.right:
                backtrack(node.right, level + 1)
        backtrack(root, 0)
        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i].reverse()
        return levels


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(13)
root.left.right = TreeNode(6)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
Solution().zigzagLevelOrder(root)
