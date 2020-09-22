# -*- coding: utf-8 -*-
"""

   File Name：     findNumbers
   Author :       jing
   Date：          2020/4/3
"""


class Solution:
    def findNumbers(self, nums) -> int:
        if nums is None or len(nums) == 0:
            return 0
        res = 0
        for num in nums:
            if self.isOdd(num):
                res += 1
        return res

    def isOdd(self, num):
        count = 1
        while num > 0:
            num = num // 10
            if num > 0:
                count += 1
            else:
                break
        return True if count % 2 == 0 else False


print(Solution().findNumbers([12,345,2,6,7896]))
