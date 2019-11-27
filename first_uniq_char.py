# -*- coding: utf-8 -*-
"""

   File Name：     first_uniq_char
   Author :       jing
   Date：          2019-11-26
   字符串中的第一个唯一字符
   https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/275/string/1143/
"""


class Solution:
    def firstUniqChar(self, s):
        if s is None or len(s) == 0:
            return -1
        else:
            if len(s) == 1:
                return 0
            else:
                d = {}
                for i in s:
                    if d.get(i):
                        d[i] = d[i]+1
                    else:
                        d[i] = 1
                for t in range(len(s)):
                    if d.get(s[t]) == 1:
                        return t
                return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar("loveleetcode"))
