# -*- coding: utf-8 -*-
"""

   File Name：     uniquePaths
   Author :       jing
   Date：          2020/3/20

   https://leetcode-cn.com/explore/interview/card/tencent/226/dynamic-programming/936/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n-1][m-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 2))
