# -*- coding: utf-8 -*-
"""
File Name:    sort-array-by-parity-ii.py
Author :      jynnezhang
Date:         2020/11/12 9:37 下午
Description:
https://leetcode-cn.com/problems/sort-array-by-parity-ii/
"""


class Solution:
    def sortArrayByParityII(self, A):
        if not A or len(A) == 0 or len(A) % 2 != 0:
            return A
        even = []
        odd = []
        for index, v in enumerate(A):
            if index % 2 == 0:
                if v % 2 == 0:
                    continue
                else:
                    even.append(index)
            if index % 2 != 0:
                if v % 2 != 0:
                    continue
                else:
                    odd.append(index)
        for i in range(len(even)):
            A[even[i]], A[odd[i]] = A[odd[i]], A[even[i]]
        return A


if __name__ == '__main__':
    print(Solution().sortArrayByParityII([648,831,560,986,192,424,997,829,897,843]))
    ret = {"1": 1}
    s = set()
    s.add(1)
    print(type(list(s)))
    for key, value in ret.items():
        print(key, 1, value)

