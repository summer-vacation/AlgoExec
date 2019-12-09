# -*- coding: utf-8 -*-
"""

   File Name：     plus_one
   Author :       jing
   Date：          2019-12-09
   https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/
"""


"""
1、[1, 2, 3]
2、[1, 9, 9]
3、[9, 9, 9]
"""


class Solution:
    def plusOne(self, digits):
        length = len(digits)
        last = 0
        for i in range(length, 0, -1):
            if digits[i-1] == 9:
                last = 9
                digits[i-1] = 0
                if i - 1 == 0:
                    digits.insert(0, 1)
            elif last == 9:
                last = digits[i - 1]
                digits[i - 1] += 1
                break
            elif i == length:
                digits[i - 1] += 1
                break

        return digits


if __name__ == '__main__':
    print(Solution().plusOne([2,4,9,3,9]))

