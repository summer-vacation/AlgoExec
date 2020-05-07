# -*- coding: utf-8 -*-
"""
File Name:    constructArr.py
Author :      jynnezhang
Date:         2020/5/1 5:49 下午
Description:

构建乘积数组
https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

除自身外其他所有数的乘积
"""


class Solution:
    def constructArr(self, a):
        copy = a[:]
        before = 1
        lens = len(copy)
        for i in range(1, lens):
            before = before * a[i-1]
            copy[i] = before
        after = 1
        for j in range(lens-2, -1, -1):
            after = after * a[j+1]
            copy[j] *= after
        copy[0] = after
        return copy

    def constructArr2(self, a):
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]  # 下三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]  # 上三角
            b[i] *= tmp  # 下三角 * 上三角
        return b

    def constructArr3(self, a):
        if not a:
            return []
        if len(a) == 1:
            return [0]
        b = [1] * len(a)
        for i in range(len(b) - 2, -1, -1):
            b[i] = b[i + 1] * a[i + 1]
        tmp = a[0]
        for j in range(1, len(a)):
            b[j] = tmp * b[j]
            tmp = tmp * a[j]
        return b


print(Solution().constructArr([7, 2, 2, 4, 2, 1, 8, 8, 9, 6, 8, 9, 6, 3, 2, 1]))
# [286654464,1003290624,1003290624,501645312,1003290624,2006581248,250822656,250822656,222953472,334430208,250822656,222953472,334430208,668860416,1003290624,2006581248]
