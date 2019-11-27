# -*- coding: utf-8 -*-
"""

   File Name：     reverse_string
   Author :       jing
   Date：          2019-11-26
   反转字符串，使用 O(1) 的额外空间
   https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/275/string/1144/
"""


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        if s is None:
            return None
        else:
            return s.reverse()


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)

