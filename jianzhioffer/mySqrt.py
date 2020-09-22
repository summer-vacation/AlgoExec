# -*- coding: utf-8 -*-
"""
File Name:    mySqrt.py
Author :      jynnezhang
Date:         2020/5/9 9:12 上午
Description:

x 的平方根

https://leetcode-cn.com/problems/sqrtx/
"""
import math


class Solution:
    """
        x^(1/2) = [e^(lnx)]^(1/2) = [e^(1/2)]^lnx
    """
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

    def mySqrt2(self, x: int) -> int:
        if x <= 0 or x == 1:
            return x
        target = 0
        for i in range(x):
            if i * i <= x:
                target = i
            else:
                break
        return target

    """
        二分查找！
    """
    def mySqrt3(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x // 2

        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left
