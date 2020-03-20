# -*- coding: utf-8 -*-
"""

   File Name：     isPowerOfTwo
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/942/
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(536870912))
