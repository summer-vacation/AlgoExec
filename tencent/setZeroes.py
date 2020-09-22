# -*- coding: utf-8 -*-
"""

   File Name：     setZeroes
   Author :       jing
   Date：          2020/4/10


"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0 or matrix[0] is None or len(matrix[0]) == 0:
            return matrix

        rows, cols = len(matrix), len(matrix[0])
        markZero = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    markZero.append((row, col))
                col += 1
            row += 1

        for position in markZero:
            self.setZero(matrix, position[0], position[1], rows, cols)

    def setZero(self, matrix, i, j, rows, cols):
        for x in range(rows):
            matrix[x][j] = 0
        for y in range(cols):
            matrix[i][y] = 0


Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])

s = "string"
list(s).sort()
res = "".join(s)
print("".join((lambda x: (x.sort(), x)[1])(list(s))))
