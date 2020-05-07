# -*- coding: utf-8 -*-
"""
File Name:    isValidBST.py
Author :      jynnezhang
Date:         2020/5/5 2:18 下午
Description:

验证二叉搜索树
https://leetcode-cn.com/problems/validate-binary-search-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        # return self.help(root)

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

    #  有问题！！！  左子树的所有结点都应该小于root！！，，
    #  下面只是判断的当前结点、左右结点的关系！
    def help(self, cur):
        cur_stat = False
        if cur is None:
            return True
        if cur.left is None and cur.right and cur.val < cur.right.val:
            cur_stat = True
        elif cur.right is None and cur.left and cur.left.val < cur.val:
            cur_stat = True
        elif cur.left and cur.right and cur.left.val < cur.val < cur.right.val:
            cur_stat = True
        elif cur.left is None and cur.right is None:
            cur_stat = True
        else:
            cur_stat = False
        return cur_stat and self.help(cur.left) and self.help(cur.right)


"""
class Solution {
    long pre = Long.MIN_VALUE;
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        // 访问左子树
        if (!isValidBST(root.left)) {
            return false;
        }
        // 访问当前节点：如果当前节点小于等于中序遍历的前一个节点，说明不满足BST，返回 false；否则继续遍历。
        if (root.val <= pre) {
            return false;
        }
        pre = root.val;
        // 访问右子树
        return isValidBST(root.right);
    }
}
"""

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
print(Solution().isValidBST(root))
