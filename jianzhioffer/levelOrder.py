# -*- coding: utf-8 -*-
"""
File Name:    levelOrder.py
Author :      jynnezhang
Date:         2020/4/28 8:06 下午
Description:

树的层序遍历
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return None
        queue = [root]
        res = [root.val]
        while queue:
            for cur in queue:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    res.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    res.append(node.right.val)
        return res


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(Solution().levelOrder(root))
