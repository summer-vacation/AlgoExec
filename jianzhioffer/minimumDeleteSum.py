# -*- coding: utf-8 -*-
"""
File Name:    minimumDeleteSum.py
Author :      jynnezhang
Date:         2020/5/25 1:16 下午
Description:
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if s1 is None and s2 is None:
            return 0

        len1, len2 = len(s1), len(s2)
        dp = [[0 for i in range(len2+1)] for j in range(len1+1)]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if i == 1:
                    dp[0][j] = dp[0][j-1] + ord(s2[j-1])
                if j == 1:
                    dp[i][0] = dp[i-1][0] + ord(s1[i-1])
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 保留时s2
                    a = dp[i-1][j] + ord(s1[i-1])
                    # 保留时s1
                    b = dp[i][j-1] + ord(s2[j-1])
                    dp[i][j] = a if a < b else b
        return dp[len1][len2]


if __name__ == '__main__':
    Solution().minimumDeleteSum("delete", "leet")
