# -*- coding: utf-8 -*-
"""

   File Name：     numRookCaptures
   Author :       jing
   Date：          2020/3/26
"""


class Solution:
    def numRookCaptures(self, board) -> int:
        if board is None or len(board) == 0 or board[0] is None or len(board) == 0:
            return 0
        p_posi = [-1, -1]
        num = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    p_posi = [i, j]
        if p_posi == [-1, -1]:
            return 0
        return self.search(board, p_posi[0], p_posi[1], num)

    def search(self, board, x, y, num):
        if x < 0 or y < 0 or x > 8 or y > 8:
            return 0
        for i in range(y, 0, -1):
            if board[x][i] == "p":
                num += 1
                break
            if board[x][i] == "B":
                break
        for j in range(y, 8, 1):
            if board[x][j] == "p":
                num += 1
                break
            if board[x][j] == "B":
                break
        for k in range(x, 0, -1):
            if board[k][y] == "p":
                num += 1
                break
            if board[k][y] == "B":
                break
        for m in range(x, 8, 1):
            if board[m][y] == "p":
                num += 1
                break
            if board[m][y] == "B":
                break
        return num


board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(Solution().numRookCaptures(board))
