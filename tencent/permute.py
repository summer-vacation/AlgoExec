# -*- coding: utf-8 -*-
"""

   File Name：     permute
   Author :       jing
   Date：          2020/3/24

   https://leetcode-cn.com/problems/permutations

   list全排列
"""


class Solution:
    def permute(self, nums):
        import itertools
        res = set(itertools.permutations(nums))
        return sorted(list(res))


print(Solution().permute([1,2,3]))
