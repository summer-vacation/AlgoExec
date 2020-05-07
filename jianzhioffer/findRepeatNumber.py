# -*- coding: utf-8 -*-
"""
File Name:    findRepeatNumber.py
Author :      jynnezhang
Date:         2020/5/1 4:05 下午
Description:

数组中重复的数字

https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
"""


class Solution:
    def findRepeatNumber(self, nums) -> int:
        if nums is None or len(nums) == 0:
            return -1
        hasmap = {}
        for num in nums:
            if num in hasmap:
                return num
            else:
                hasmap[num] = 0
