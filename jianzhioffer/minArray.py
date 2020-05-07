# -*- coding: utf-8 -*-
"""
File Name:    minArray.py
Author :      jynnezhang
Date:         2020/4/30 12:42 下午
Description:

旋转数组的最小数字
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
"""


class Solution:
    def minArray(self, numbers) -> int:
        if numbers is None:
            return 0
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0]


print(Solution().minArray([2,2,2,0,1]))
