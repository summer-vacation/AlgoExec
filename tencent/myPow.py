# -*- coding: utf-8 -*-
"""

   File Name：     myPow
   Author :       jing
   Date：          2020/3/27

   https://leetcode-cn.com/problems/powx-n/

   Pow(x, n)

   需要考虑整数、负数、分数
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


print(Solution().myPow(26.00000, 7))
