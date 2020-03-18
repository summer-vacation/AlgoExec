# -*- coding: utf-8 -*-
"""

   File Name：     two_sum
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/894/

   返回的是索引
   只有一个结果
   不能利用相同的数字
"""


class Solution:
    def twoSum(self, nums, target: int):
        if nums is None or len(nums) < 2:
            return []
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        """
        """
        for i in range(len(nums)):
            j = nums.index(target-nums[1])
            if j:
                return [i, j]
        """
        # dict hashtable更快！！！
        dict = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dict:
                return dict[a], i
            else:
                dict[nums[i]] = i


if __name__ == '__main__':
    print(Solution().twoSum([-1,-2,-3,-4,-5], -8))
