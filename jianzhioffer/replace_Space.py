# -*- coding: utf-8 -*-
"""

   File Name：     replace_space
   Author :       jing
   Date：          2020/3/15

   将空格替换成%20
"""


class Solution:
    # s 源字符串
    # O(n)的方法：计算字符串长度、空格长度，从后往前替换
    def replaceSpace(self, s):
        # write code here
        if s is None or s == "":
            return s
        else:
            return s.replace(" ", "%20")
