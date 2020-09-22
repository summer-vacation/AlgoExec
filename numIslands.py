# -*- coding: utf-8 -*-
"""

   File Name：     numIslands
   Author :       jing
   Date：          2020/3/23
"""


class Solution:
    def numIslands(self, grid) -> int:
        if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        island_num = 0
        new_grid = []
        for i in range(rows + 2):
            row = []
            for j in range(cols + 2):
                if i == 0 or i == len(grid) + 1:
                    row.append(0)
                elif j == 0 or j == len(grid[0]) + 1:
                    row.append(0)
                else:
                    row.append(grid[i - 1][j - 1])
            new_grid.append(row)
        for i in range(1, rows + 2):
            for j in range(1, cols + 2):
                if new_grid[i][j] == '1':
                    island_num += 1
                    self.update_around(new_grid, i, j)
                    continue
                if new_grid[i][j] == '99':
                    self.update_around(new_grid, i, j)
                    continue
        return island_num

    def update_around(self, grid, i, j):
        grid[i][j] = '99'
        if grid[i - 1][j] == '1':
            grid[i - 1][j] = '99'
        if grid[i][j - 1] == '1':
            grid[i][j - 1] = '99'
        if grid[i + 1][j] == '1':
            grid[i + 1][j] = '99'
        if grid[i][j + 1] == '1':
            grid[i][j + 1] = '99'

    def numIslands2(self, grid) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > '0':
                    counter += 1
                    self.dfs(grid, i, j)
        return counter

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)


if __name__ == '__main__':
    # print(Solution().numIslands([
    #     ['1','1','1','1','0'],
    #     ['1','1','0','1','0'],
    #     ['1','1','0','0','0'],
    #     ['0','0','0','0','0'],
    # ]))

    print(Solution().numIslands2([["1","1","1"],["0","1","0"],["1","1","1"]]))
