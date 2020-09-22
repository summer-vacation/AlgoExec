# -*- coding: utf-8 -*-
"""

   File Name：     buildTree
   Author :       jing
   Date：          2020/3/24

   https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

   通过前序和中序，构造初二叉树
"""
from tencent.sort_and_search.TreeNode import TreeNode

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if preorder is None or inorder is None or len(preorder) != len(inorder) or len(preorder) == 0:
            return None
        root = preorder[0]
        divide_index_in = inorder.index(root)
        left = self.buildTree(preorder[1:1+divide_index_in], inorder[0:divide_index_in])
        right = self.buildTree(preorder[1+divide_index_in:], inorder[divide_index_in+1:])
        result = TreeNode(root)
        result.left = left
        result.right = right
        return result


if __name__ == '__main__':
    tree = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(tree.val)
    print(tree.left.val)
    print(tree.right.val)
