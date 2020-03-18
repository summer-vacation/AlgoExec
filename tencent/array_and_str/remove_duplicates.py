# -*- coding: utf-8 -*-
"""

   File Name：     remove_duplicates
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/902/
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        if nums is None or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        index = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[index]:
                continue
            else:
                index += 1
                nums[index] = nums[i]
        return index+1


if __name__ == '__main__':
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
