# -*- coding: utf-8 -*-
"""
File Name:    find-the-longest-substring-containing-vowels-in-even-counts.py
Author :      jynnezhang
Date:         2020/11/13 3:20 下午
Description:
https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for index, c in enumerate(s):
            if c in vowels.keys():
                if vowels[c]%2 == 0:
                    max_len = max(max_len, index - start + 1)
                else:
                    pass
                vowels[c] += 1
            else:
                max_len += 1


