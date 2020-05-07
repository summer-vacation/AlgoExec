# -*- coding: utf-8 -*-
"""

   File Name：     pathSum
   Author :       jing
   Date：          2020/4/13

   二叉树中和为某一值的路径

   https://leetcode-cn.com/problems/path-sum-ii/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if root is None:
            return []
        res = []
        path = []
        self.help(root, sum, path, res)
        return res

    def help(self, root, expectNumber, path, res):
        path.append(root.val)
        if root.left is None and root.right is None and sum(path) == expectNumber:
            res.append(list(path))
        temp = path[:]
        if root.left:
            self.help(root.left, expectNumber, path, res)
        path = temp[:]
        if root.right:
            self.help(root.right, expectNumber, path, res)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
print(Solution().pathSum(root, 22))
