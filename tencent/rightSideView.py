
# -*- coding: utf-8 -*-
"""

   File Name：     rightSideView
   Author :       jing
   Date：          2020/4/22

   https://leetcode-cn.com/problems/binary-tree-right-side-view/
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode):
        rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 由于每一层最后一个访问到的节点才是我们要的，因此不断更新对应深度的信息即可
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

print(Solution().rightSideView(root))
