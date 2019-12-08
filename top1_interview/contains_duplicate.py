# -*- coding: utf-8 -*-
"""

   File Name：     contains_duplicate
   Author :       jing
   Date：          2019-12-08
   https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/
"""


class Solution:
    def containsDuplicate(self, nums) -> bool:
        nondup = set(nums)
        if len(nondup) == len(nums):
            return False
        else:
            return True


if __name__ == '__main__':
    print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
