# -*- coding: utf-8 -*-
"""

   File Name：     containsNearbyDuplicate
   Author :       jing
   Date：          2020/3/31
"""


class Solution:
    # 超时
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if nums is None or len(nums) < 2:
            return False
        for i in range(len(nums)):
            n = nums[i]
            if n in nums[i+1:]:
                index = nums[i+1:].index(n)
                if index+1 <= k:
                    return True
        return False

    def containsNearbyDuplicate2(self, nums, k):
        dictionary = {}
        for key, value in enumerate(nums):
            if value in dictionary and key - dictionary[value] <= k:
                return True
            dictionary[value] = key
        return False


print(Solution().containsNearbyDuplicate2([1,2,3,1,2,3], 2))
