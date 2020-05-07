# -*- coding: utf-8 -*-
"""
File Name:    twoSum.py
Author :      jynnezhang
Date:         2020/5/2 9:06 下午
Description:


和为s的两个数字
https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return []
        i, j = 0, len(nums)-1
        while i < j:
            cur_s = nums[i] + nums[j]
            if cur_s > target:
                j -= 1
            elif cur_s < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []

