# -*- coding: utf-8 -*-
"""

   File Name：     search
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/927/

   搜索旋转排序数组
    O(log n)
"""


class Solution:
    def search(self, nums, target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        if target in nums:
            index = nums.index(target)
            return index
        else:
            return -1

    # 二分搜索
    def search2(self, nums, target: int) -> int:
            if not nums:
                return -1
            if len(nums) == 1:
                return 0 if nums[0] == target else -1
            cent = len(nums) // 2
            if target < nums[cent] <= nums[-1]:
                return self.search(nums[:cent], target)
            elif target >= nums[cent] >= nums[0]:
                res = self.search(nums[cent:], target)
                if res == -1:
                    return -1
                else:
                    return cent + res
            else:
                resl = self.search(nums[:cent], target)
                resr = self.search(nums[cent:], target)
                if resr != -1:
                    return cent + resr
                if resl != -1:
                    return resl
            return -1


if __name__ == '__main__':
    print(Solution().search([4,5,6,7,0,1,2], 3))

