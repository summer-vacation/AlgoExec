# -*- coding: utf-8 -*-
"""

   File Name：     reverse
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/938/
"""


class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            x = -x
            negative = True
        str_x = str(x)

        res = int(str_x[::-1])
        if res > 2 ** 31 - 1 or res < - 2 ** 31:
            res = 0

        return res if not negative else -1 * res


if __name__ == '__main__':
    print(Solution().reverse(123000))
