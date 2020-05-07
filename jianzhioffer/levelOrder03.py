# -*- coding: utf-8 -*-
"""
File Name:    levelOrder03.py
Author :      jynnezhang
Date:         2020/4/29 10:59 上午
Description:

层序遍历，每一层放在一个list

之字形打印
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        queue = [root]
        res = []
        level_flag = 1
        while queue:
            level = []
            level_lens = len(queue)
            for i in range(level_lens):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_flag % 2 == 0:
                res.append(level[::-1])
            else:
                res.append(level)
            level_flag += 1
        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))
