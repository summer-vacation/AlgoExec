# -*- coding: utf-8 -*-
"""

   File Name：     shell_sort
   Author :       jing
   Date：          2020/3/31
"""


def shell_sort(nums):
    n = len(nums)
    gap = n // 2
    while gap:
        for i in range(gap, n):
            while i - gap >= 0 and nums[i - gap] > nums[i]:
                nums[i - gap], nums[i] = nums[i], nums[i - gap]
                i -= gap
        gap //= 2
    return nums
