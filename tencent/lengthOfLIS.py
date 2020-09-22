# -*- coding: utf-8 -*-
"""

   File Name：     lengthOfLIS
   Author :       jing
   Date：          2020/3/24
   https://leetcode-cn.com/problems/longest-increasing-subsequence/

   最长上升子序列
"""


class Solution:
    def lengthOfLIS(self, nums) -> int:
        if nums is None or len(nums) == 0:
            return 0
        # 从尾到头比较
        dp = [1 for i in range(len(nums))]
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
