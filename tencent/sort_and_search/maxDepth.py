# -*- coding: utf-8 -*-
"""

   File Name：     maxDepth
   Author :       jing
   Date：          2020/3/20

   https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/930/
   二叉树深度
"""

from tencent.sort_and_search.TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(2)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(3)
    print(Solution().maxDepth(root))
