# -*- coding: utf-8 -*-
"""

   File Name：     3sum
   Author :       jing
   Date：          2020/3/17
   https://leetcode.com/problems/3sum/
    考虑k num 问题！！
"""


class Solution:
    def __init__(self):
        self.result = []

    def threeSum(self, nums):
        lens = len(nums)
        nums.sort()
        i = 0
        while i < lens-2:
            self.twoSum(nums, i+1, 0 - nums[i])
            while i < lens - 2 and nums[i] == nums[i+1]:
                i += 1
            i += 1

        return self.result

    def twoSum(self, nums, start, res):
        left = start
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == res:
                self.result.append([nums[start-1], nums[left], nums[right]])
                while left < right and nums[left+1] == nums[left]:
                    left += 1
                while left < right and nums[right-1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > res:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
