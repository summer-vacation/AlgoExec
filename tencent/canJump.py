# -*- coding: utf-8 -*-
"""
   File Name：     canJump
   Author :       jing
   Date：          2020/4/20

"""


class Solution:
    def canJump(self, nums) -> bool:
        if nums is None or len(nums) == 0:
            return True
        for index, i in enumerate(nums):
            if i >= len(nums):
                return True
            for gap in range(1, i):
                return self.help(index, nums, gap, len(nums))
        return False

    def help(self, index, nums, gap, totalLens):
        if index + gap >= totalLens:
            return True
        else:
            n = list(nums[index+gap:])
            if index + n[index] >= totalLens - 1:
                return True
            for ii in range(n[index]):
                if index + ii >= totalLens-1:
                    return True
                else:
                    return self.help(index, n, ii, len(n))


print(Solution().canJump([3,2,1,0,4]))
