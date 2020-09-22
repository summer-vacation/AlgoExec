# -*- coding: utf-8 -*-
"""

   File Name：     kthSmallest
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/929/

   二叉搜索树中第K小的元素
"""

from tencent.sort_and_search.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.res = []

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.dfs(root)
        if len(self.res) >= k:
            return self.res[k-1]
        return -1

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Solution().kthSmallest(root, 4))
