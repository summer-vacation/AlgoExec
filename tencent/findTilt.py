# -*- coding: utf-8 -*-
"""

   File Name：     findTilt
   Author :       jing
   Date：          2020/3/24
"""
from tencent.sort_and_search.TreeNode import TreeNode

tilt_tree = 0

class Solution:

    def findTilt(self, root: TreeNode) -> int:
        global tilt_tree
        if root is None:
            return 0
        self.traverse(root)
        return tilt_tree

    def traverse(self, root):
        global tilt_tree
        if root is None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        tilt_tree += abs(left - right)
        return left + right + root.val


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.right = TreeNode(3)
    print(Solution().findTilt(root))
