# -*- coding: utf-8 -*-
"""
File Name:    countSmaller.py
Author :      jynnezhang
Date:         2020/9/25 1:15 下午
Description:

https://leetcode-cn.com/leetbook/read/top-interview-questions/xajl22/
"""


class Solution:
    def countSmaller(self, nums):
        result = []
        new_nums = nums[::-1]
        for index, num in enumerate(new_nums):
            _c = 0
            while index > 0:
                index -= 1
                if num > new_nums[index]:
                    _c += 1

            result.append(_c)
        return result[::-1]


if __name__ == '__main__':
    print(Solution().countSmaller([2,0,1]))
