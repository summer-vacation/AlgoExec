# -*- coding: utf-8 -*-
"""
File Name:    maximum-gap.py
Author :      jynnezhang
Date:         2020/11/26 9:38 上午
Description:
https://leetcode-cn.com/problems/maximum-gap/
"""


class Solution:
    def maximumGap(self, nums) -> int:
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        print(nums)
        max_res = 0
        for i in range(1, len(nums)):
            max_res = max(nums[i] - nums[i-1], max_res)
        return max_res


if __name__ == '__main__':
    print(Solution().maximumGap([3,6,9,1]))

