# -*- coding: utf-8 -*-
"""

   File Name：     palindrome_number
   Author :       jing
   Date：          2020/3/17

   https://leetcode.com/problems/palindrome-number/
   判断数字是否是回文数
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isPalindrome(-121))
