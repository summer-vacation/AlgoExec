# -*- coding: utf-8 -*-
"""

   File Name：     remove_duplicates
   Author :       jing
   Date：          2019-12-08
   https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                j += 1
                nums[j] = nums[i]
        return j+1


if __name__ == '__main__':
    res = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(res))
    print(res)
