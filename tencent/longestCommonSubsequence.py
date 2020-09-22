# -*- coding: utf-8 -*-
"""

   File Name：     longestCommonSubsequence
   Author :       jing
   Date：          2020/3/24

   https://leetcode-cn.com/problems/longest-common-subsequence/

   最长公共子序列
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 is None or text2 is None or len(text1) == 0 or len(text2) == 0:
            return 0
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0 for i in range(len1+1)] for j in range(len2+1)]

        for i in range(1, len2+1):
            for j in range(1, len1+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().longestCommonSubsequence("abcde", "ace"))

