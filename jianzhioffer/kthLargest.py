# -*- coding: utf-8 -*-
"""
File Name:    kthLargest.py
Author :      jynnezhang
Date:         2020/4/30 10:02 上午
Description:

二叉搜索树的第k大节点
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return None
        res = []
        self.preOrder(root, res)
        if k > len(res):
            return None
        else:
            return res[len(res)-k]

    def preOrder(self, cur, res):
        if cur is None:
            return 0
        self.preOrder(cur.left, res)
        res.append(cur.val)
        self.preOrder(cur.right, res)

    # 提前返回！
    def kthLargest2(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.k = k
        self.res = 0
        dfs(root)
        return self.res
