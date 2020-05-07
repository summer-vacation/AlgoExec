# -*- coding: utf-8 -*-
"""

   File Name：     sumKPath
   Author :       jing
   Date：          2020/3/23
   二叉树中和为k的路径

"""

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        ret, trace = [], []
        if root:
            self.dfs(root, expectNumber, ret, trace)
        return ret

    def dfs(self, root, n, ret, trace):
        trace.append(root.val)
        if (root.left == None) and (root.right == None):
            if n == root.val:
                ret.append(trace[:])        # 深拷贝
        if root.left:
            self.dfs(root.left, n - root.val, ret, trace)
        if root.right:
            self.dfs(root.right, n - root.val, ret, trace)
        trace.pop()
