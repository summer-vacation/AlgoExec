# -*- coding: utf-8 -*-
"""

   File Name：     subarraySum
   Author :       jing
   Date：          2020/4/11
"""


class Solution:
    # 超时
    def subarraySum(self, nums, k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        count = 0
        for index, n in enumerate(nums):
            cur_sum = 0
            for m in nums[index:]:
                cur_sum += m
                if cur_sum == k:
                    count += 1

        return count

    def subarraySum2(self, nums, k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        all_sum = {0: 1}
        cur_sum = 0
        count = 0
        for n in nums:
            cur_sum += n

            if cur_sum - k in all_sum.keys():
                count += all_sum[cur_sum - k]
            if cur_sum in all_sum.keys():
                all_sum[cur_sum] += 1
            else:
                all_sum[cur_sum] = 1
        return count


print(Solution().subarraySum2([1,1,1], 2))
