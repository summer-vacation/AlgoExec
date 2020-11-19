# -*- coding: utf-8 -*-
"""
File Name:    move-zeroes.py
Author :      jynnezhang
Date:         2020/11/19 1:39 下午
Description:
https://leetcode-cn.com/problems/move-zeroes/
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums)-1, -1, -1):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
        return nums


if __name__ == '__main__':
    print(Solution().moveZeroes([0,1,0,3,12]))
