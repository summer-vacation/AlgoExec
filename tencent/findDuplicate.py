# -*- coding: utf-8 -*-
"""

   File Name：     findDuplicate
   Author :       jing
   Date：          2020/3/24

   https://leetcode-cn.com/problems/find-the-duplicate-number/

   寻找重复数
"""


class Solution:
    def findDuplicate(self, nums) -> int:
        if nums is None or len(nums) < 2:
            return None
        num_dict = {}
        for n in nums:
            if n not in num_dict:
                num_dict[n] = 1
            else:
                return n
        return None
