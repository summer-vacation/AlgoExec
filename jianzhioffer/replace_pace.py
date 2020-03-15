# -*- coding: utf-8 -*-
"""

   File Name：     replace_pace
   Author :       jing
   Date：          2020/3/15
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if s is None or s == "":
            return s
        else:
            return s.replace(" ", "%20")
