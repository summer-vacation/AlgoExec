# -*- coding: utf-8 -*-
"""

   File Name：     merge
   Author :       jing
   Date：          2020/4/16

   https://leetcode-cn.com/problems/merge-intervals/

   合并区间

   输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""


class Solution:
    def merge(self, intervals):
        if intervals is None or intervals[0] is None or len(intervals) == 0 or len(intervals[0]) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        result = []
        result.append(list(intervals[0]))
        i = 0
        for index, interval in enumerate(intervals):
            if index == 0:
                continue
            if result[i][0] <= interval[0] <= result[i][1] <= interval[1]:
                result[i][1] = interval[1]
            elif result[i][0] <= interval[0] <= interval[1] <= result[i][1]:
                continue
            else:
                result.append(list(interval))
                i += 1
        return result


print(Solution().merge([[1, 4], [1, 5]]))
