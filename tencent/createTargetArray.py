# -*- coding: utf-8 -*-
"""

   File Name：     createTargetArray
   Author :       jing
   Date：          2020/4/3

   https://leetcode-cn.com/problems/create-target-array-in-the-given-order/submissions/
"""


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return []
        lens_n = len(nums)
        target = []
        for i in range(lens_n):
            if index[i] - len(target) == 1 or index[i] == len(target):
                target.append(nums[i])
            elif index[i] < len(target):
                if target[index[i]] == "#":
                    target[index[i]] = nums[i]
                target.insert(index[i], nums[i])
            else:
                for i in range(index[i]):
                    target.append("#")
                target.append(nums[i])
        return target
