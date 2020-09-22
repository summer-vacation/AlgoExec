# -*- coding: utf-8 -*-
"""

   File Name：     rand10
   Author :       jing
   Date：          2020/3/27

   https://leetcode-cn.com/problems/implement-rand10-using-rand7/
"""


class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        res = self.rand40()
        while res >= 40:
            res = self.rand40()
        return res % 10 + 1

    def rand40(self):
        res = 7 * (rand7() - 1) + rand7() - 1
        return res
