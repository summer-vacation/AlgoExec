# -*- coding: utf-8 -*-
"""
File Name:    count-complete-tree-nodes.py
Author :      jynnezhang
Date:         2020/11/24 9:36 上午
Description:完全二叉树的节点数

https://leetcode-cn.com/problems/count-complete-tree-nodes/
"""
from jianzhioffer.isBalanced import TreeNode


class Solution:
    counts = 0

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        self.counts = left + right + 1
        return self.counts


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(Solution().countNodes(root))
