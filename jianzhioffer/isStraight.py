# -*- coding: utf-8 -*-
"""
File Name:    isStraight.py
Author :      jynnezhang
Date:         2020/4/30 12:33 下午
Description:

扑克牌中的顺子

https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
"""


class Solution:
    def isStraight(self, nums) -> bool:
        repeat = set()
        max_, min_ = 0, 14
        for num in nums:
            if num == 0:
                continue   # 跳过大小王
            max_ = max(max_, num)   # 最大牌
            min_ = min(min_, num)   # 最小牌
            if num in repeat:
                return False    # 若有重复，提前返回 false
            repeat.add(num)     # 添加牌至 Set
        return max_ - min_ < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


print(Solution().isStraight([0, 0, 2, 2, 5]))
