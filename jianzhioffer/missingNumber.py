# -*- coding: utf-8 -*-
"""

   File Name：     missingNumber
   Author :       jing
   Date：          2020/4/13

   0～n-1中缺失的数字
   https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        len_n = len(nums)
        sum_n = (0 + len_n) * (len_n+1) // 2
        sum_nn = 0
        for n in nums:
            sum_nn += n
        return sum_n - sum_nn


