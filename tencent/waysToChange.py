# -*- coding: utf-8 -*-
"""

   File Name：     waysToChange
   Author :       jing
   Date：          2020/4/23

   https://leetcode-cn.com/problems/coin-lcci

    输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1

"""


class Solution:
    def waysToChange(self, n: int) -> int:
        if n <= 0:
            return 0
        dp = [0 for n in range(n+1)]
        coin = [1, 5, 10, 25]
        dp[0] = 1
        for i in range(4):
            for j in range(coin[i], n+1):
                # if i >= coin[j]:
                dp[j] = (dp[j]+dp[j-coin[i]]) % 1000000007
        return dp[n]


print(Solution().waysToChange(5))
