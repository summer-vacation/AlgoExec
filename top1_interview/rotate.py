# -*- coding: utf-8 -*-
"""

   File Name：     rotate
   Author :       jing
   Date：          2019-12-08
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/
原list上修改

"""


class Solution:
    def rotate1(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = len(nums)

        if k == num / 2:
            for i in range(int(num/2)):
                target = (i + k) % num
                temp = nums[i]
                nums[i] =nums[target]
                nums[target] = temp
        else:
            flags = []
            j = 0
            temp1 = nums[j]
            for i in range(num):
                flags.append("0")
            while str(flags).find("0") != -1:
                if flags[j] == "0":
                    flags[j] = "1"
                    target = (j + k) % num
                    j = target
                    temp2 = nums[target]
                    nums[target] = temp1
                    temp1 = temp2
                else:
                    j = flags.index("0")
                    temp1 = nums[j]
        return nums

    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        nums.reverse()
        left = nums[:k]
        right = nums[k:]
        left.reverse()
        right.reverse()
        nums[:k] = left
        nums[k:] = right
        return nums


if __name__ == '__main__':
    print(Solution().rotate([1,2], 3))

#  654321
