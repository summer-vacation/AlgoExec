# -*- coding: utf-8 -*-
"""

   File Name：     is_palindrome
   Author :       jing
   Date：          2019-11-25
   验证回文字符串
   https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/275/string/1136/
"""

import re


class Solution:
    def isPalindrome(self, s):
        if s is None:
            return True
        else:
            s = s.lower()           # 小写和空格
            s = re.sub("[^a-z0-9]", "", s)      # 去掉符号
            # print(s)
            # print(s[::-1])
            if s == s[::-1]:
                return True
            else:
                return False


if __name__ == '__main__':
    print(Solution().isPalindrome("race a car"))

