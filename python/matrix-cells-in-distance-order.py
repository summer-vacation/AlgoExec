# -*- coding: utf-8 -*-
"""
File Name:    matrix-cells-in-distance-order.py
Author :      jynnezhang
Date:         2020/11/17 1:35 下午
Description:
https://leetcode-cn.com/problems/matrix-cells-in-distance-order/
"""


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        result = []
        for i in range(R):
            for j in range(C):
                result.append([i, j])
        result.sort(key=lambda x: (abs(x[0]-r0)+abs(x[1]-c0)))
        return result


if __name__ == '__main__':
    print(Solution().allCellsDistOrder(R = 2, C = 2, r0 = 0, c0 = 1))
