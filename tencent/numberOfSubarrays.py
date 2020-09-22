# -*- coding: utf-8 -*-
"""

   File Name：     numberOfSubarrays
   Author :       jing
   Date：          2020/4/21

   https://leetcode-cn.com/problems/count-number-of-nice-subarrays/
"""


class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        if nums is None or len(nums) < k:
            return 0
        count = 0
        index_odd = []
        i = 0
        while i < len(nums):
            if self.isOdd(nums[i]):
                index_odd.append(i)
            i += 1
        if len(index_odd) < k:
            return 0
        for i in range(k-1, len(index_odd)):
            count += 1
            if i == k-1:
                left = index_odd[i - k + 1]
            else:
                left = index_odd[i - k + 1] - index_odd[i - k] - 1
            if i == len(index_odd)-1:
                right = len(nums) - index_odd[i] - 1
            else:
                right = index_odd[i+1] - index_odd[i] - 1
            count += left + right + left * right
        return count

    def isOdd(self, num):
        return True if num % 2 == 1 else False


print(Solution().numberOfSubarrays([1,1,2,1,1], 3))
