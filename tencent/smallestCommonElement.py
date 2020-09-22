# -*- coding: utf-8 -*-
"""

   File Name：     smallestCommonElement
   Author :       jing
   Date：          2020/4/7
"""


class Solution:
    def smallestCommonElement(self, mat) -> int:
        if mat is None or len(mat) == 0 or mat[0] is None or len(mat[0]) == 0:
            return None
        value_count = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] not in value_count.keys():
                    value_count[mat[i][j]] = 1
                else:
                    value_count[mat[i][j]] = value_count.get(mat[i][j]) + 1
        min_co = 100000
        for key, value in value_count.items():
            if value == len(mat) and key < min_co:
                min_co = key
        return min_co


print(Solution().smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]))
