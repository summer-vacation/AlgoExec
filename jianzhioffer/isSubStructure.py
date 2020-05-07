# -*- coding: utf-8 -*-
"""
File Name:    isSubStructure.py
Author :      jynnezhang
Date:         2020/4/29 6:52 下午
Description:

子树:
递归，


https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None or B is None:
            return False
        if self.recur(A, B):
            return True
        else:
            return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def recur(self, A, B):
        if B is None:
            return True
        if A is None or A.val != B.val:
            return False
        return self.recur(A.left, B.left) and self.recur(A.right, B.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
B = TreeNode(2)
B.left = TreeNode(1)
print(Solution().isSubStructure(root, B))
