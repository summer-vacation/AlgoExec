# -*- coding: utf-8 -*-
"""

   File Name：     lowestCommonAncestor02
   Author :       jing
   Date：          2020/3/20

   https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/934/

   二叉树的最近公共祖先
"""
from tencent.sort_and_search.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif not left:
            return right
        elif not right:
            return left


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    print(Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(2)))
