# -*- coding: utf-8 -*-
"""
File Name:    largest-perimeter-triangle.py
Author :      jynnezhang
Date:         2020/11/29 12:55 下午
Description:
https://leetcode-cn.com/problems/largest-perimeter-triangle/
"""


class Solution:
    def largestPerimeter(self, A=[]) -> int:
        if not A or len(A) < 3:
            return 0
        A.sort(reverse=True)
        i = 2
        while i < len(A):
            a1, a2, a3 = A[i-2], A[i-1], A[i]
            if a2 + a3 > a1:
                return a1 + a2 + a3
            else:
                i += 1
        return 0


if __name__ == '__main__':
    print(Solution().largestPerimeter([3,6,2,3]))
