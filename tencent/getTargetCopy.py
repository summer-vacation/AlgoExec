# -*- coding: utf-8 -*-
"""

   File Name：     getTargetCopy
   Author :       jing
   Date：          2020/4/5


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return None
        return self.preorder(original, cloned, target)

    def preorder(self, original, cloned, target):
        if original == target:
            return cloned
        if original is None:
            return
        res_left = self.preorder(original.left, cloned.left, target)
        res_right = self.preorder(original.right, cloned.right, target)
        return res_left if res_left else res_right


original = TreeNode(7)
original.left = TreeNode(4)
original.right = TreeNode(3)
original.right.left = TreeNode(6)
original.right.right = TreeNode(19)

cloned = TreeNode(7)
cloned.left = TreeNode(4)
cloned.right = TreeNode(3)
cloned.right.left = TreeNode(6)
cloned.right.right = TreeNode(19)

Solution().getTargetCopy(original, cloned, original.right)
