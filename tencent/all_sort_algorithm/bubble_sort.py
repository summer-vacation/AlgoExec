# -*- coding: utf-8 -*-
"""

   File Name：     bubble_sort
   Author :       jing
   Date：          2020/3/31

"""


def bubble_sort(nums):
    n = len(nums)
    # 进行多次循环
    for c in range(n):
        for i in range(1, n - c):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
    return nums


if __name__ == '__main__':
    print(bubble_sort([10, 44, 56, 1, 9, 4, 12, 6, 7]))
