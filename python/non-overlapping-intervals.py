# -*- coding: utf-8 -*-
"""
File Name:    non-overlapping-intervals.py
Author :      jynnezhang
Date:         2020/11/16 1:00 下午
Description:
https://leetcode-cn.com/problems/non-overlapping-intervals/
"""


class Solution:
    def eraseOverlapIntervals(self, intervals=[]):
        if intervals is None or len(intervals) == 0:
            return 0
        nums = len(intervals)
        intervals.sort(key=lambda x: x[1])
        pre = intervals[0][1]
        total = 0
        for i in range(1, nums):
            if intervals[i][0] < pre:
                total += 1
            else:
                pre = intervals[i][1]
        return total


if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals([[1,2], [1,3], [3,4], [1,3]]))


