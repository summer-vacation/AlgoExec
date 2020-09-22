# -*- coding: utf-8 -*-
"""

   File Name：     selection_sort
   Author :       jing
   Date：          2020/3/31

   选择排序
"""

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

