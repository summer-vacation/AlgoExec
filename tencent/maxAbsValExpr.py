# -*- coding: utf-8 -*-
"""

   File Name：     maxAbsValExpr
   Author :       jing
   Date：          2020/4/2
"""


class Solution:
    def maxAbsValExpr(self, arr1, arr2) -> int:
        if arr1 is None or len(arr1) == 0:
            return 0
        len_n = len(arr1)
        if len_n == 1:
            return 0
        max_val = -1
        for i in range(len_n - 1):
            for j in range(i+1, len_n):
                cur_val = abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j)
                if cur_val > max_val:
                    max_val = cur_val
        return max_val


print(Solution().maxAbsValExpr(arr1 = [1,2,3,4], arr2 = [-1,4,5,6]))
