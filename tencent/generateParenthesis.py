# -*- coding: utf-8 -*-
"""

   File Name：     generateParenthesis
   Author :       jing
   Date：          2020/4/6

   https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/92/
   生成括号
   排列组合
"""


class Solution:
    def generateParenthesis(self, n: int):
        List = []
        self.help(0, 0, "", List, n)
        return List

    def help(self, left, right, res, l, n):
        if left < right:
            return
        if left == n and right == n:
            l.append(res)
            return
        if left > n or right > n:
            return

        self.help(left + 1, right, res + '(', l, n)
        self.help(left, right + 1, res + ')', l, n)
        return res


print(Solution().generateParenthesis(2))
