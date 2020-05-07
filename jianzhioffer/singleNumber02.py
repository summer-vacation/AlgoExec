# -*- coding: utf-8 -*-
"""

   File Name：     singleNumber02
   Author :       jing
   Date：          2020/4/13

   数组中数字出现的次数 II

   https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/

   一个数字只出现一次之外，其他数字都出现了三次。
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1

        mapper = {}
        for n in nums:
            if n in mapper.keys():
                mapper[n] += 1
            else:
                mapper[n] = 1
        for key, value in mapper.items():
            if value == 1:
                return key
