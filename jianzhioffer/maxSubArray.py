# -*- coding: utf-8 -*-
"""
File Name:    maxSubArray.py
Author :      jynnezhang
Date:         2020/5/2 9:33 上午
Description:

最大子序列和

https://leetcode-cn.com/problems/maximum-subarray/
https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        if nums is None or len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return nums[0]
        lens = len(nums)
        dp = [0 for i in range(lens)]       # 当前index为结尾的最大和，状态转移方程 dp[i] = max(dp[i-1] + nums[i], nums[i])
        dp[0] = nums[0]
        max_val = nums[0]
        for i in range(1, lens):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_val = max(max_val, dp[i])
        return max_val


if __name__ == '__main__':
    print(Solution().maxSubArray([1,2]))
