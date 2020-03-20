# -*- coding: utf-8 -*-
"""

   File Name：     lowestCommonAncestor
   Author :       jing
   Date：          2020/3/20

   https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/933/

   二叉搜索树的最近公共祖先
"""

from tencent.sort_and_search.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.left is None or root.right is None:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(3)
    root.right.right.right = TreeNode(5)
    print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val)
