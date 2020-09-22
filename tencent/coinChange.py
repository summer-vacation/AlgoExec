# -*- coding: utf-8 -*-
"""

   File Name：     coinChange
   Author :       jing
   Date：          2020/3/27

   https://leetcode-cn.com/problems/coin-change/
"""
import math


class Solution:
    #  动态规划
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        dp = list()
        temp = amount + 1

        for i in range(amount + 1):
            if i not in coins:
                dp.append(temp)
            else:
                dp.append(1)

        for i in range(amount + 1):
            if i not in coins:
                for j in coins:
                    if i - j > 0:
                        dp[i] = min(dp[i - j] + 1, dp[i])

        return dp[amount] if dp[amount] != temp else -1

    # 用的类似的方法，但是是用目标值-coin，超时了……
    def coinChange2(self, coins, amount: int) -> int:
        if coins is None or len(coins) == 0 or amount < 1:
            return 0

        from collections import deque
        queue = deque([(0, 0)])
        visited = set([0])
        while queue:

            cur, step = queue.popleft()
            if cur == amount:
                return step
            if cur > amount:
                continue

            for coin in coins:
                value = cur + coin
                if value not in visited:
                    visited.add((value))
                    queue.append((value, step + 1))

        return -1


if __name__ == '__main__':
    print(Solution().coinChange2([1, 2, 5], amount=100))
