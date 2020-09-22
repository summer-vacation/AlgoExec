# -*- coding: utf-8 -*-
"""

   File Name：     permute01
   Author :       jing
   Date：          2020/4/6
"""


class Solution:
    def permute(self, nums):
        if nums is None or len(nums) < 2:
            return nums
        res = []
        cur = []
        lens = len(nums)
        flag = [False for i in range(lens)]
        self.help(nums, res, cur, flag, lens)
        return res

    def help(self, nums, res, cur, flag, targetlens):
        if len(cur) == targetlens:
            res.append(list(cur))
            return
        for i in range(targetlens):
            if not flag[i]:
                flag[i] = True
                cur.append(nums[i])
                self.help(nums, res, cur, flag, targetlens)
                cur.remove(nums[i])
                flag[i] = False

pp = []
str1 = "abs"
pp.append(str1)
str1 += "11"
str1 = str1[:-1]
print(pp)
print(str1)
ppp = set([])

print(Solution().permute([1,2,3]))
