# -*- coding: utf-8 -*-
"""

   File Name：     generate_matrix
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/913/
"""

class Solution:
    def generateMatrix(self, n: int):
        if n == 0:
            return [[]]
        elif n == 1:
            return [[1]]

        matrix = [["#" for i in range(n)] for i in range(n)]
        cnt = 1
        left = 0
        right = n-1
        top = 0
        down = n-1
        state = "right"
        x, y = 0, 0
        while cnt <= n * n:
            if matrix[x][y] == "#":
                matrix[x][y] = cnt
                cnt += 1
            if state == "right":
                y += 1
                if y > right:
                    state = "down"
                    y -= 1
                    top += 1
            elif state == "down":
                x += 1
                if x > down:
                    state = "left"
                    right -= 1
                    x -= 1
            elif state == "left":
                y -= 1
                if left > y:
                    state = "up"
                    down -= 1
                    y += 1
            elif state == "up":
                x -= 1
                if top > x:
                    state = "right"
                    left += 1
                    x += 1

        return matrix


if __name__ == '__main__':
    print(Solution().generateMatrix(3))

