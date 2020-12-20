# -*- coding: utf-8 -*-
"""

   File Name：     countPrimes
   Author :       jing
   Date：          2020/4/13

   https://leetcode-cn.com/problems/count-primes/

   质数
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_primes = [True for i in range(n)]
        is_primes[0] = False
        is_primes[1] = False

        i = 2
        while i*i < n:
            if not is_primes[i]:
                continue
            j = i * i
            while j < n:
                is_primes[j] = False
                j += i
            i += 1
        count = 0
        for i in range(2, n):
            if is_primes[i]:
                count += 1
        return count


print(Solution().countPrimes(11))

