# -*- coding: utf-8 -*-
"""
   File Name：     myPow
   Author :       jing
   Date：          2020/4/13

   https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
   https://leetcode-cn.com/problems/powx-n/
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1
        if n == 2:
            return x * x
        return self.myPow(self.myPow(x, n//2), 2) if not n % 2 else x * self.myPow(self.myPow(x, n // 2), 2)
