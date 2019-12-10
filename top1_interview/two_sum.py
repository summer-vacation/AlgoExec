# -*- coding: utf-8 -*-
"""

   File Name：     two_sum
   Author :       jing
   Date：          2019-12-08
   https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum1(self, nums, target: int):
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i+1:]:
                index = nums.index(res, i + 1)
                return i, index
            else:
                continue

    def twoSum(self, nums, target: int):
        num_dict = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in num_dict:
                return [num_dict[res], i]
            else:
                num_dict[nums[i]] = i


if __name__ == '__main__':
    print(Solution().twoSum([3,2,4], 6))
