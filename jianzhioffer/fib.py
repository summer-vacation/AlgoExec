# -*- coding: utf-8 -*-
"""
File Name:    fib.py
Author :      jynnezhang
Date:         2020/4/30 11:16 上午
Description:

斐波那契

递归会超时！
https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
https://leetcode-cn.com/problems/fibonacci-number/
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

    def fib2(self, n):
        if n == 0 or n == 1:
            return n
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a + b
        return b


print(Solution().fib2(5))
