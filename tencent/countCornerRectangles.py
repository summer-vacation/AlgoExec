# -*- coding: utf-8 -*-
"""

   File Name：     countCornerRectangles
   Author :       jing
   Date：          2020/4/21

   https://leetcode-cn.com/problems/number-of-corner-rectangles/
"""


class Solution:
    def countCornerRectangles(self, grid) -> int:
        if grid is None or len(grid) < 1 or grid[0] is None or len(grid[0]) < 1:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                for m in range(1, rows - i):
                    for n in range(1, cols - j):
                        if self.isCornerRectangles(i, j, m, n, grid):
                            count += 1
        return count

    def isCornerRectangles(self, x0, y0, m, n, grid):
        if grid[x0][y0] == 1 and grid[x0 + m][y0] == 1 and grid[x0][y0 + n] == 1 and grid[x0 + m][y0 + n] == 1:
            return True


print(Solution().countCornerRectangles([[0,1,0],
                                        [1,0,1],
                                        [1,0,1],
                                        [0,1,0]]))
