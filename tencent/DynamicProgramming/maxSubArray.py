# -*- coding: utf-8 -*-
"""

   File Name：     maxSubArray
   Author :       jing
   Date：          2020/3/20

   https://leetcode-cn.com/explore/interview/card/tencent/226/dynamic-programming/922/

   最大子序列和
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        if nums is None:
            return -1
        elif len(nums) < 2:
            return nums[0]
        lens = len(nums)
        dp = [0 for i in range(lens)]       # 当前index为结尾的最大和，状态转移方程 dp[i] = max(dp[i-1] + nums[i], nums[i])
        dp[0] = nums[0]
        max_val = nums[0]
        for i in range(1, lens):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_val = max(max_val, dp[i])
        return max_val


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


