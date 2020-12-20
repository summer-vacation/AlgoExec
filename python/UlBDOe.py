# -*- coding: utf-8 -*-
"""
File Name:    UlBDOe.py
Author :      jynnezhang
Date:         2020/11/19 5:18 下午
Description:
https://leetcode-cn.com/problems/UlBDOe/
"""
import re


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        pattern = r"[r]+[y]+[r]+"
        match = re.findall(pattern, leaves)
        if len(match) == 1:
            return 0
        no_r = 0
        for index, c in enumerate(leaves):
            pass


if __name__ == '__main__':
    print(Solution().minimumOperations('rrryyyrryyyrr'))
