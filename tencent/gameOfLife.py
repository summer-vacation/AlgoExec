# -*- coding: utf-8 -*-
"""

   File Name：     gameOfLife
   Author :       jing
   Date：          2020/4/2
"""


class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0 or board[0] is None or len(board[0]) == 0:
            return board
        modify = {}
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                self.updateAround(board, i, j, modify, rows, cols)

        for key, val in modify.items():
            board[key[0]][key[1]] = val
        return board

    def updateAround(self, board, i, j, modify, rows, cols):
        total = 0
        for k in range(i - 1, i + 2):
            if k < 0 or k > rows - 1:
                continue
            for m in range(j - 1, j + 2):
                if m < 0 or m > cols - 1:
                    continue
                if k == i and m == j:
                    continue
                if board[k][m] == 1:
                    total += 1
        if board[i][j] == 1:
            if total < 2:
                modify[(i, j)] = 0
            elif total > 3:
                modify[(i, j)] = 0
        if board[i][j] == 0:
            if total == 3:
                modify[(i, j)] = 1


print(Solution().gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))
