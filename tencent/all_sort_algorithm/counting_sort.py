# -*- coding: utf-8 -*-
"""

   File Name：     counting_sort
   Author :       jing
   Date：          2020/3/31
"""


def counting_sort(nums):
    if not nums: return []
    n = len(nums)
    _min = min(nums)
    _max = max(nums)
    tmp_arr = [0] * (_max - _min + 1)
    for num in nums:
        tmp_arr[num - _min] += 1
    j = 0
    for i in range(n):
        while tmp_arr[j] == 0:
            j += 1
        nums[i] = j + _min
        tmp_arr[j] -= 1
    return nums
