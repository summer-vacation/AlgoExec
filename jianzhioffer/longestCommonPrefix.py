# -*- coding: utf-8 -*-
"""
File Name:    longestCommonPrefix.py
Author :      jynnezhang
Date:         2020/5/9 9:21 下午
Description:

最长公共前缀

https://leetcode-cn.com/problems/longest-common-prefix
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        s = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(s) != 0:
                s = s[:-1]
        return s

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]


s = ""
s.startswith()
