# -*- coding: utf-8 -*-
"""
File Name:    diameterOfBinaryTree.py
Author :      jynnezhang
Date:         2020/5/9 9:00 下午
Description:

二叉树的直径:
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

两节点的最长路径

https://leetcode-cn.com/problems/diameter-of-binary-tree/
"""


class Solution:
    def __init__(self):
        self.max_ = 0

    def diameterOfBinaryTree(self, root):
        self.height(root)
        return self.max_

    def height(self, root):
        if root is None:
            return 0
        if root.left == root.right:
            return 1
        left = self.height(root.left)
        right = self.height(root.right)
        self.max_ = max(left+right, self.max_)
        return max(left, right) + 1

    def diameterOfBinaryTree2(self, root):
        self.ans = 1

        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
