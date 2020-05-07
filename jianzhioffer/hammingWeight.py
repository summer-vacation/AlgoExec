# -*- coding: utf-8 -*-
"""
File Name:    hammingWeight.py
Author :      jynnezhang
Date:         2020/4/30 12:01 下午
Description:

数的二进制表示中1的个数

&  位计算，与，，都1则1

"""


class Solution:
    # 利用n与n-1的关系
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

    # 逐位比较
    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


print(Solution().hammingWeight(3))
