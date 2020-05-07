# -*- coding: utf-8 -*-
"""

   File Name：     findNthDigit
   Author :       jing
   Date：          2020/4/13

   https://leetcode-cn.com/problems/nth-digit/

   数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

    请写一个函数，求任意第n位对应的数字。

"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        # 首先判断第n的数是几位数的数字target里的，用digits表示
        base = 9
        digits = 1
        while n - base * digits > 0:        # 0-9，1位数，，9+90*2，2位数，，9+90*2+900*3，3位数
            n -= base * digits
            base *= 10
            digits += 1
        # 计算target的值
        idx = n % digits  # 注意由于上面的计算，n现在表示digits位数的第n个数字
        if idx == 0:
            idx = digits
        number = 1
        for i in range(1, digits):
            number *= 10
        if idx == digits:
            number += n // digits - 1
        else:
            number += n // digits
        # 找到target中对应的数字
        for i in range(idx, digits):
            number //= 10
        return number % 10


print(Solution().findNthDigit(191))
