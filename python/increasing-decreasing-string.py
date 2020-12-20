# -*- coding: utf-8 -*-
"""
File Name:    increasing-decreasing-string.py
Author :      jynnezhang
Date:         2020/11/25 11:13 上午
Description:
https://leetcode-cn.com/problems/increasing-decreasing-string/
"""


class Solution:
    def sortString(self, s: str) -> str:
        sorted_s = sorted(list(s))
        print(sorted_s)
        res = ""
        while len(sorted_s) > 1:
            res += sorted_s[0]
            sorted_s.pop(0)
            i = 0
            while i < len(sorted_s):
                print(sorted_s[i], res[-1])
                if sorted_s[i] > res[-1]:
                    res += sorted_s[i]
                    sorted_s.pop(i)
                else:
                    i += 1
            if len(sorted_s) == 0:
                break
            res += sorted_s[len(sorted_s)-1]
            sorted_s.pop(len(sorted_s)-1)
            j = len(sorted_s) - 1
            while j > -1:
                if sorted_s[j] < res[-1]:
                    res += sorted_s[j]
                    sorted_s.pop(j)
                j -= 1
            if len(sorted_s) == 0:
                break
        return res + "".join(sorted_s)


if __name__ == '__main__':
    print(Solution().sortString("rat"))
