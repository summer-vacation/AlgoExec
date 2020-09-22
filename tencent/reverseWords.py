# -*- coding: utf-8 -*-
"""

   File Name：     reverseWords
   Author :       jing
   Date：          2020/3/31

   翻转
   https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ""
        list_s = s.split()      # 按空格拆分，已经去掉了多余的空格
        res = ""
        for ls in list_s:
            res = ls + " " + res
        return res[:-1]

    def reverseWords2(self, s: str) -> str:
        return " ".join(s.split()[::-1])


print(Solution().reverseWords2("a good   example"))
