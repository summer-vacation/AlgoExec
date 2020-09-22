# -*- coding: utf-8 -*-
"""

   File Name：     majorityElement
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/941/

   个数超过一半的数
"""
import collections


class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement2(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # 计数
    def majorityElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        mydict = {}
        n = len(nums) // 2
        for i in range(len(nums)):
            if nums[i] not in mydict:
                mydict[nums[i]] = 1
            else:
                mydict[nums[i]] += 1
                if mydict[nums[i]] > n:
                    return nums[i]
