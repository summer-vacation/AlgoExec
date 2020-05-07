# -*- coding: utf-8 -*-
"""
File Name:    minNumber.py
Author :      jynnezhang
Date:         2020/4/28 8:18 下午
Description:
"""


class Solution:
    def minNumber(self, nums) -> str:
        if nums is None or len(nums) == 0:
            return None
        res = []
        cur = []
        lens = len(nums)
        flag = [False for i in range(lens)]
        self.permute(nums, flag, cur, res)
        min_ = 2 ** 32
        for r in res:
            ss = ""
            for x in r:
                ss += str(x)
            if int(ss) < int(min_):
                min_ = ss
        return min_

    def permute(self, nums, flag, cur, res):
        if len(cur) == len(nums):
            res.append(list(cur))
        for i in range(len(nums)):
            if not flag[i]:
                flag[i] = True
                cur.append(nums[i])
                self.permute(nums, flag, cur, res)
                cur.remove(nums[i])
                flag[i] = False

    def minNumber2(self, nums) -> str:
        import functools

        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)

    def minNumber3(self, nums) -> str:
        def fast_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            fast_sort(l, i - 1)
            fast_sort(i + 1, r)

        strs = [str(num) for num in nums]
        fast_sort(0, len(strs) - 1)
        return ''.join(strs)


print(Solution().minNumber2([3, 30, 34, 5, 9]))
