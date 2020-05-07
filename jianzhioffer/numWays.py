# -*- coding: utf-8 -*-
"""
File Name:    numWays.py
Author :      jynnezhang
Date:         2020/4/30 12:17 下午
Description:

青蛙跳台阶问题

https://leetcode-cn.com/problems/climbing-stairs/
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
"""


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1 or n == 2:
            return n
        m, k = 1, 2
        i = 3
        while i <= n:
            m, k = k, m + k
            i += 1
        return k % 1000000007


print(Solution().numWays(7))
