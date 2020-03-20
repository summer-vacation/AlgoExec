# -*- coding: utf-8 -*-
"""

   File Name：     majorityElement
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/941/

   个数超过一半的数
"""


class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

