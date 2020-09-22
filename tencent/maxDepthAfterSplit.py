# -*- coding: utf-8 -*-
"""

   File Name：     maxDepthAfterSplit
   Author :       jing
   Date：          2020/4/1

https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
   有效括号的嵌套深度

   分成两组，对半分的时候 Depth最小

   因为一组较多，depth就会增加
"""


class Solution:
    def maxDepthAfterSplit(self, seq: str):
        res = [0 for _ in range(len(seq))]
        cnt = 0
        for i, x in enumerate(seq):
            if x == "(":
                cnt += 1
                res[i] = cnt % 2
            else:
                res[i] = cnt % 2
                cnt -= 1
        return res
