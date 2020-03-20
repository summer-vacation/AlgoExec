# -*- coding: utf-8 -*-
"""

   File Name：     spiral_order
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/912/
"""

class Solution:
    def spiralOrder(self, matrix):
        if matrix is None or len(matrix) == 0:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        result = []
        cnt = 0
        left = 0
        right = n-1
        top = 0
        down = m-1
        state = "right"
        x, y = 0, 0
        while cnt < m * n:
            if matrix[x][y] != "#":
                result.append(matrix[x][y])
                matrix[x][y] = "#"
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

        return result


if __name__ == '__main__':
    print(len([]))
    input = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
    print(Solution().spiralOrder(input))
