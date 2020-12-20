# -*- coding: utf-8 -*-
"""
File Name:    wiggle-subsequence.py
Author :      jynnezhang
Date:         2020/12/12 1:52 下午
Description:
https://leetcode-cn.com/problems/wiggle-subsequence/
"""


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return 1
        max_len = 0
        pre_status = None
        first_index = 0
        for index, num in enumerate(nums):
            if index == 0:
                continue
            if index == 1:
                pre_status = True if num - nums[index - 1] > 0 else False
                first_index = index - 1
            else:
                cur = True if num - nums[index - 1] > 0 else False
                if cur != pre_status:
                    max_len += 1
                    pre_status = cur
                else:
                    first_index = index - 1
                    max_len = max(max_len, index - first_index + 1)
        return max_len


if __name__ == '__main__':
    print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    l = []
    ll = [1,2,3]
    l.extend(ll)
    print(l)
