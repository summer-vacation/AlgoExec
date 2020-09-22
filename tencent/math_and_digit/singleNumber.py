# -*- coding: utf-8 -*-
"""

   File Name：     singleNumber
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/940/

   找出只出现一次的数
"""


class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num
        return result
