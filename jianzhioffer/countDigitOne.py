# -*- coding: utf-8 -*-
"""
File Name:    countDigitOne.py
Author :      jynnezhang
Date:         2020/4/29 7:38 下午
Description:
从1到n，所有数字含有1的个数

https://leetcode-cn.com/problems/number-of-digit-one/
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        number = 0
        for i in range(1, n+1):
            number += number_of_1(i)
        return number

    def countDigitOne2(self, n: int) -> int:
        if n <= 0: return 0

        num_s = str(n)
        high = int(num_s[0])
        Pow = 10 ** (len(num_s) - 1)
        last = n - high * Pow

        if high == 1:
            return self.countDigitOne2(Pow - 1) + self.countDigitOne2(last) + last + 1
        else:
            return Pow + high * self.countDigitOne2(Pow - 1) + self.countDigitOne2(last)


def number_of_1(n):
    """
    n这个数字中出现1的次数
    :param n: 输入的整数
    """
    num = 0
    while n > 0:
        # 获得余数，若余数为1，则次数加1
        if n % 10 == 1:
            num += 1
        n = n // 10
    return num


print(Solution().countDigitOne2(99))
