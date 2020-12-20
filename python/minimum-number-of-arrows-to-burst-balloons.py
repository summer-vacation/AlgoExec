# -*- coding: utf-8 -*-
"""
File Name:    minimum-number-of-arrows-to-burst-balloons.py
Author :      jynnezhang
Date:         2020/11/23 3:34 下午
Description:
https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""


class Solution:
    def findMinArrowShots(self, points) -> int:
        """
        排序：按照结束位置
        贪心：每次选择最末尾的位置射箭，这样覆盖的气球范围最广
        :param points:
        :return:
        """
        if not points and len(points) == 0:
            return 0
        points.sort(key=lambda x: (x[1]))
        arrow = 1
        arrow_pos = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= arrow_pos <= points[i][1]:
                continue
            else:
                arrow += 1
                arrow_pos = points[i][1]
        return arrow


if __name__ == '__main__':
    print(Solution().findMinArrowShots(points=[[1,2],[2,3],[3,4],[4,5]]))
