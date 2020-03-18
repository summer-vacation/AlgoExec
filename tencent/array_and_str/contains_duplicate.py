# -*- coding: utf-8 -*-
"""

   File Name：     contains_duplicate
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/908/
"""


class Solution:
    def containsDuplicate(self, nums) -> bool:
        if nums is None or len(nums) == 0 or len(nums) == 1:
            return False
        nums.sort()
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return True
            left += 1
            right += 1
        return False

    def containsDuplicate2(self, nums) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True


if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,1]))
