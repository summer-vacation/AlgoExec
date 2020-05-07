# -*- coding: utf-8 -*-
"""

   File Name：     maxValue
   Author :       jing
   Date：          2020/4/13
"""


class Solution:
    def maxValue(self, grid) -> int:
        if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for m in range(cols)] for n in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                if i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                    continue
                if j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                    continue
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[rows-1][cols-1]


print(Solution().maxValue([
  [1]
]))
