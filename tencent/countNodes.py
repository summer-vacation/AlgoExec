# -*- coding: utf-8 -*-
"""

   File Name：     countNodes
   Author :       jing
   Date：          2020/3/24
"""
from tencent.sort_and_search.TreeNode import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    print(Solution().countNodes(root))
