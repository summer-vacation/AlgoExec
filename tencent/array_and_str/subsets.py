# -*- coding: utf-8 -*-
"""
File Name:    subsets.py
Author :      jynnezhang
Date:         2020/9/20 11:23 上午
Description:

子集

https://leetcode-cn.com/problems/subsets/
"""


class Solution:
    def subsets(self, nums):
        if nums is None:
            return None
        result = []
        item = []
        result.append(list(item))
        if len(nums) == 0:
            return result
        self.generate(0, nums, item, result)
        return result

    def generate(self, i, nums, item, result):
        if i >= len(nums):
            return
        item.append(nums[i])
        result.append(list(item))
        self.generate(i + 1, nums, item, result)
        item.pop()
        self.generate(i + 1, nums, item, result)


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
