# -*- coding: utf-8 -*-
"""

   File Name：     subsets
   Author :       jing
   Date：          2020/3/20

   https://leetcode-cn.com/explore/interview/card/tencent/226/dynamic-programming/937/

   不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

   说明：解集不能包含重复的子集。
"""


class Solution:
    def subsets(self, nums):
        if nums is None:
            return None
        result = []
        item = []
        result.append(list(item))
        if len(nums) == 0:
            return result
        self.generate(0, nums, item, result)
        return result

    def generate(self, i, nums, item, result):
        if i >= len(nums):
            return
        item.append(nums[i])
        result.append(list(item))
        self.generate(i + 1, nums, item, result)
        item.pop()
        self.generate(i + 1, nums, item, result)

    def subsets2(self, nums):
        if nums is None:
            return []
        res = []
        cur = []
        flag = [False for i in range(len(nums))]
        self.help(nums, res, cur, flag)
        result = []
        for cur in res:
            item = []
            for i in range(len(cur)):
                if cur[i] == "1":
                    item.append(nums[i])
            result.append(item)

        return res, result

    def help(self, nums, res, cur, flag):
        if len(cur) == len(nums):
            res.append(list(cur))
            return
        for i in range(len(nums)):
            if not flag[i]:
                flag[i] = True
                cur.append(1)
                self.help(nums, res, cur, flag)
                cur[i] = 0
                flag[i] = False


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
