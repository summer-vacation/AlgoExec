# -*- coding: utf-8 -*-
"""

   File Name：     move_zeroes
   Author :       jing
   Date：          2019-12-09
   https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/567/
"""
"""
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

in-place
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0
        for i in range(len(nums)):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1
        return nums


if __name__ == '__main__':
    print(Solution().moveZeroes([0,0,1]))

