# -*- coding: utf-8 -*-
"""

   File Name：     exist
   Author :       jing
   Date：          2020/4/26

   矩阵中的路径
"""

class Solution:
    def exist(self, board, word: str) -> bool:
        if board is None or len(board) == 0 or board[0] is None or len(board[0]) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.path(board, i, j, word, 0):
                    return True
        return False

    def path(self, board, x, y, word, index):
        if x < 0 or y < 0 or x > len(board) - 1 or y > len(board[0]) - 1:
            return False
        if board[x][y] == word[index]:
            if index == len(word) - 1:
                return True
            else:
                val = board[x][y]
                board[x][y] = "#"
                ###  这样写会超时！！！！每一个condition都会计算！
                top_condition = self.path(board, x-1, y, word, index + 1)
                left_condition = self.path(board, x, y - 1, word, index + 1)
                below_condition = self.path(board, x+1, y, word, index + 1)
                right_condition = self.path(board, x, y + 1, word, index + 1)
                board[x][y] = val
                return top_condition or left_condition or below_condition or right_condition
        else:
            return False


class Solution:
    def exist(self, board, word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


print(Solution().exist(board = [["a","b"],["c","d"]], word = "abcd"))
