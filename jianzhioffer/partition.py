# -*- coding: utf-8 -*-
"""
File Name:    partition.py
Author :      jynnezhang
Date:         2020/5/7 6:48 下午
Description:

分割回文串

https://leetcode-cn.com/problems/palindrome-partitioning/
"""


class Solution:
    def partition(self, s: str):
        if s is None or len(s) == 0:
            return []
        out = []
        for i in range(0, len(s)):
            if self.isPalindrome(s[:i+1]):
                res = [s[:i+1]]
                self.recur(s[i + 1:], res, out)
                # out.append(list(self.recur(s[i+1:], res, out)))

        return out

    def recur(self, s, res, out):
        if s == "":
            out.append(list(res))
            # return res
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                res.append(s[:i+1])
                self.recur(s[i+1:], res, out)
                res.pop()
        # return res

    def isPalindrome(self, s):
        return True if s == s[::-1] else False


print(Solution().partition("cdd"))
print(Solution().partition("a"))
print(Solution().partition("aab"))
