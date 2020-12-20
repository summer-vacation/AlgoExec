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


if __name__ == '__main__':
    print(selection_sort([10, 44, 56, 1, 1, 9, 4, 12, 6, 7]))
