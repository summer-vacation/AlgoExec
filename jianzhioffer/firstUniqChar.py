# -*- coding: utf-8 -*-
"""
File Name:    firstUniqChar.py
Author :      jynnezhang
Date:         2020/5/2 10:00 上午
Description:
第一个只出现一次的字符

https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '

    # 有序字典
    def firstUniqChar2(self, s: str) -> str:
        import collections
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v:
                return k
        return ' '
