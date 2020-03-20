# -*- coding: utf-8 -*-
"""

   File Name：     isPalindrome
   Author :       jing
   Date：          2020/3/19

   https://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/939/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)


if __name__ == '__main__':
    print(Solution().isPalindrome(121))
