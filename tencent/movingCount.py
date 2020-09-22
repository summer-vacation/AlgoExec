# -*- coding: utf-8 -*-
"""

   File Name：     movingCount
   Author :       jing
   Date：          2020/4/8

   https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int):
        if m < 1 and n < 1:
            return 0
        if k < 0:
            return 0
        dp = [[False for i in range(n)] for j in range(m)]
        self.dfs(0, 0, k, dp, m, n)
        count = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j]:
                    count += 1
        return count

    def dfs(self, x, y, target, dp, m, n):
        if x < 0 or x >= m or y < 0 or y >= n:
            return
        if self.canIn(x, y, target):
            if not dp[x][y]:
                dp[x][y] = True
            else:
                return
        else:
            return
        self.dfs(x - 1, y, target, dp, m, n)
        self.dfs(x + 1, y, target, dp, m, n)
        self.dfs(x, y - 1, target, dp, m, n)
        self.dfs(x, y + 1, target, dp, m, n)

    def canIn(self, x, y, tartget):
        sum_nm = 0
        while x > 0:
            sum_nm += x % 10
            x = x // 10
        while y > 0:
            sum_nm += y % 10
            y = y // 10
        return sum_nm <= tartget


print(Solution().movingCount(1, 2, 1))
