# -*- coding: utf-8 -*-
"""

   File Name：     findKthLargest
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/928/
    数组中的第K个最大元素
"""


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        if k == 1 and len(nums) == 1:
            return nums[k]
        nums.sort(reverse=True)
        return nums[k-1]


if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
