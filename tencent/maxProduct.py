# -*- coding: utf-8 -*-
"""

   File Name：     maxProduct
   Author :       jing
   Date：          2020/3/25

   https://leetcode-cn.com/problems/maximum-product-subarray/

   乘积最大子数组
"""


class Solution:
    # 因为负负得正，两个负数可能隔开了，所以需要记录每一个位置的最大值和最小值
    def maxProduct(self, nums) -> int:
        if nums is None or len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]
        max_dp = nums[:]
        min_dp = nums[:]
        max_res = max_dp[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1] * nums[i], nums[i], min_dp[i-1] * nums[i])
            min_dp[i] = min(min_dp[i-1] * nums[i], nums[i], max_dp[i-1] * nums[i])
            max_res = max(max_dp[i], max_res)
        return max_res

