# -*- coding: utf-8 -*-
"""

   File Name：     minTimeToVisitAllPoints
   Author :       jing
   Date：          2020/4/3

   访问所有点的最小时间

   1. 每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
   2. 必须按照数组中出现的顺序来访问这些点。

   两点之间的最短距离 = max(abs(p2.x - p1.x), abs(p2.y - p1.y))
"""


class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        if points is None or len(points) < 2 or len(points[0]) < 2:
            return 0
        p_s = points[0]
        res = 0
        for i, p in enumerate(points):
            if i == 0:
                continue
            px, py = abs(p_s[0] - p[0]), abs(p_s[1] - p[1])
            line = max(px, py)
            res = res + line
            p_s = p
        return res


print(Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
