# -*- coding: utf-8 -*-
"""

   File Name：     isSubtree
   Author :       jing
   Date：          2020/4/2

   树的子结构

   给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
"""
from tencent.sort_and_search.TreeNode import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None or t is None:
            return False
        if self.isSubtree(s.left, t) or self.sameSub(s, t) or self.isSubtree(s.right, t):
            return True
        return False

    def sameSub(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False
        return self.sameSub(s.left, t.left) and self.sameSub(s.right, t.right)
