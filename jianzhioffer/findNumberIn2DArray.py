# -*- coding: utf-8 -*-
"""
   File Name：     findNumberIn2DArray
   Author :       jing
   Date：          2020/3/15

   二维数组中的查找
   https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if target is None or target == "" or array is None:
            return False
        if len(array) == 0:
            return False
        row_lens = len(array)    # 行数
        col_lens = len(array[0])
        if target < array[0][0] or target > array[row_lens-1][col_lens-1]:
            return False
        else:
            i = row_lens-1
            j = 0
            while i > 0 and j < col_lens:       # 左下角开始比
                if target == array[i][j]:
                    return True
                elif target > array[i][j]:
                    j = j + 1
                elif target < array[i][j]:
                    i = i - 1


if __name__ == '__main__':
    s = Solution()
    print(s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
