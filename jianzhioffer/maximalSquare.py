# -*- coding: utf-8 -*-
"""
File Name:    maximalSquare.py
Author :      jynnezhang
Date:         2020/5/8 8:59 下午
Description:

最大正方形

https://leetcode-cn.com/problems/maximal-square/
"""


class Solution:
    """
    动态规划，通过 min 记录正方形的边
    """
    def maximalSquare(self, matrix) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare


print(Solution().maximalSquare([[1, 0, 1, 0, 0],
                                [1, 0, 1, 1, 1],
                                [1, 1, 1, 1, 1],
                                [1, 0, 0, 1, 0]
                                ]))
