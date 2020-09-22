# -*- coding: utf-8 -*-
"""

   File Name：     decodeString
   Author :       jing
   Date：          2020/3/25

   https://leetcode-cn.com/problems/decode-string/
"""


class Solution:
    def decodeString(self, s: str) -> str:
        if s is None or len(s) == 0:
            return None

        i = 0
        res_str = ""
        loop = ""
        loop_num = 0
        while i < len(s):
            if s[i].isdigit():
                loop_num = int(s[i])
                i += 2
            if s[i].isalpha():
                loop += s[i]
                i += 1
            if s[i] == "]":
                i += 1
                for j in range(loop_num):
                    res_str += loop
                loop = ""

        return res_str


if __name__ == '__main__':
    print(Solution().decodeString("3[a]2[bc]"))
