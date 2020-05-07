# -*- coding: utf-8 -*-
"""
File Name:    sumNums.py
Author :      jynnezhang
Date:         2020/5/1 4:07 下午
Description:

求1+2+…+n

要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）

https://leetcode-cn.com/problems/qiu-12n-lcof/
"""


class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


print(Solution().sumNums(10))
