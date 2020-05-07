# -*- coding: utf-8 -*-
"""
File Name:    findContinuousSequence.py
Author :      jynnezhang
Date:         2020/5/1 1:05 下午
Description:

和为s的连续正数序列

https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
"""


class Solution:
    def findContinuousSequence(self, target: int):
        if target == 1:
            return [[1]]
        sum_n, res = [], []
        cur_sum, i = 0, 1
        while i <= target//2+2:
            if cur_sum == target:
                res.append(list(sum_n))
                cur_sum += i
                sum_n.append(i)
                i += 1
            elif cur_sum > target:
                poped = sum_n.pop(0)
                cur_sum -= poped
            if cur_sum < target:
                cur_sum += i
                sum_n.append(i)
                i += 1
                continue
        return res


print(Solution().findContinuousSequence(15))
