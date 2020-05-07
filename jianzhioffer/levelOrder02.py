# -*- coding: utf-8 -*-
"""
File Name:    levelOrder02.py
Author :      jynnezhang
Date:         2020/4/30 10:17 上午
Description:


层序遍历，，每一层放在一个list

https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        res = []
        while queue:
            level = []
            level_lens = len(queue)
            for i in range(level_lens):
                poped = queue.pop(0)
                level.append(poped.val)
                if poped.left:
                    queue.append(poped.left)
                if poped.right:
                    queue.append(poped.right)

            res.append(level)
        return res
