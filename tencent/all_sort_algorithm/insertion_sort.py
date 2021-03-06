# -*- coding: utf-8 -*-
"""

   File Name：     insertion_sort
   Author :       jing
   Date：          2020/3/31
"""


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        while i > 0 and nums[i - 1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            i -= 1
    return nums


if __name__ == '__main__':
    print(insertion_sort([10, 44, 56, 1, 9, 4, 12, 6, 7]))
