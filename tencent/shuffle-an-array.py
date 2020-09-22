# -*- coding: utf-8 -*-
"""

   File Name：     shuffle-an-array
   Author :       jing
   Date：          2020/3/25

   https://leetcode-cn.com/problems/shuffle-an-array/

   打乱数组
"""


class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.copy = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.copy

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        # import random
        # random.shuffle(self.nums)
        # return self.nums
        import random
        for i in range(len(self.nums)):
            j = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
