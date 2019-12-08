# -*- coding: utf-8 -*-
"""

   File Name：     single_number
   Author :       jing
   Date：          2019-12-08
   https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/
"""


class Solution:
    def singleNumber(self, nums) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res = res^nums[i]
        return res


if __name__ == '__main__':
    print(Solution().singleNumber([1,2,3,4,3,2,1]))
