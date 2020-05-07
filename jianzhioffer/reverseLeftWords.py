# -*- coding: utf-8 -*-
"""

   File Name：     reverseLeftWords
   Author :       jing
   Date：          2020/4/13

   左旋转字符串

   https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
