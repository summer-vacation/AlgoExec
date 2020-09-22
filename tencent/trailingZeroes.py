# -*- coding: utf-8 -*-
"""

   File Name：     trailingZeroes
   Author :       jing
   Date：          2020/3/30
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n // 5
            n //= 5
        return count;

    def trailingZeroes2(self, n: int) -> int:
        if n == 0:
            return 1
        res = self.getRes(n)
        print(res)
        str_res = str(res)
        len_n = len(str_res)
        str2 = str_res.rstrip("0")
        return len_n - len(str2)

    def getRes(self, n):
        if n == 1:
            return n
        return n * self.getRes(n-1)

print(Solution().trailingZeroes(5))
