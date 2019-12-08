# -*- coding: utf-8 -*-
"""

   File Name：     max_product
   Author :       jing
   Date：          2019-12-07
   乘积最大子序列
   https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/264/array/1126/
"""
import math


class Solution:
    """
    maxProduct1() 超时！！！
    """
    def maxProduct1(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            max = 0
            pre = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                pre = nums[i]
                if max < pre:
                    max = pre
                for j in range(i+1, len(nums)):
                    if nums[j] == 0:
                        break
                    pre = pre * nums[j]
                    if max < pre:
                        max = pre

    def maxProduct(self, A) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A), max(B))


if __name__ == '__main__':
    print(Solution().maxProduct([-2,0,-1]))

