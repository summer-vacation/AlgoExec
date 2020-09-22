# -*- coding: utf-8 -*-
"""

   File Name：     sortColors
   Author :       jing
   Date：          2020/4/7

   https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/96/

   给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
"""


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return None
        # len_n = len(nums)
        # res = [1 for i in range(len_n)]
        # right = len_n - 1
        # left = 0
        # for n in nums:
        #     if n == 2:
        #         res[right] = 2
        #         right -= 1
        #     if n == 0:
        #         res[left] = 0
        #         left += 1
        # return res

        index = 0
        count = 0
        len_n = len(nums)
        while count < len_n:
            if nums[index] == 2:
                nums.pop(index)
                nums.append(2)
            elif nums[index] == 0:
                nums.pop(index)
                nums.insert(0, 0)
                index += 1
            else:
                index += 1
            count += 1
        return nums


print(Solution().sortColors([2,0,2,1,1,0]))
