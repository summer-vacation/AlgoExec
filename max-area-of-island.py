# -*- coding: utf-8 -*-
"""

   File Name：     max-area-of-island
   Author :       jing
   Date：          2020/3/16
   https://leetcode-cn.com/problems/max-area-of-island/
   岛的最大面积
"""

class Solution:
    nextStep = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    step = 0

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.step = 0
                    self.dfs(grid, i, j)
                    res = max(res, self.step)

        return res

    def dfs(self, grid, x, y):
        """
        :type grid: List[list[int]]
        :type x: int
        :type y: int
        :rtype : None
        """
        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] != 1:
            return
        grid[x][y] = -1
        self.step += 1
        for i in range(len(self.nextStep)):
            self.dfs(grid, x + self.nextStep[i][0], y + self.nextStep[i][1])


if __name__ == '__main__':
    input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    input2 = [[1, 1, 0, 0, 0],
              [1, 1, 0, 0, 0],
              [0, 0, 0, 1, 1],
              [0, 0, 0, 1, 1]]
    input3 = [[1, 1, 1], [1, 0, 0]]
    s = Solution()
    print(s.maxAreaOfIsland(input))
