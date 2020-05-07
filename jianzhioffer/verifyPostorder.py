# -*- coding: utf-8 -*-
"""

   File Name：     verifyPostorder
   Author :       jing
   Date：          2020/4/26

   一个list是否 符合 二叉搜索树的后序遍历序列
"""


class Solution:
    def verifyPostorder(self, postorder) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            p = i
            # 所有比根节点小的都是左子树
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            # 所有比根节点大的都是右子树
            while postorder[p] > postorder[j]:
                p += 1
            # 递归每一个子树
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


print(Solution().verifyPostorder([1,3,2,6,5]))
