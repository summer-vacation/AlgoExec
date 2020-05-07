# -*- coding: utf-8 -*-
"""
File Name:    majorityElement.py
Author :      jynnezhang
Date:         2020/5/1 2:39 下午
Description:

出现次数超过一半的数字

https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
https://leetcode-cn.com/problems/majority-element/
"""


class Solution:
    def majorityElement(self, nums) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x

    def majorityElement02(self, nums) -> int:
        nums.sort()
        return nums[len(nums)//2]


# 扩展：投票法
# 如果不存在众数（原题目中已经说明一定存在），则需要验证
class Solution2:
    def majorityElement(self, nums) -> int:
        votes, count = 0, 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        # 验证 x 是否为众数
        for num in nums:
            if num == x:
                count += 1
        return x if count > len(nums) // 2 else 0 # 当无众数时返回 0

