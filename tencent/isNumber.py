# -*- coding: utf-8 -*-
"""

   File Name：     isNumber
   Author :       jing
   Date：          2020/4/26

    表示数值的字符串
"""


class Solution:
    def __init__(self):
        self.p = 0

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if s == '': return False
        number = self.scanInterger(s)

        if self.p > len(s) - 1:
            return number

        if self.p < len(s) and s[self.p] == '.':
            self.p += 1
            if self.p > len(s) - 1:
                return number
            number = self.scanUnsignedInterger(s) or number

        if self.p < len(s) and s[self.p] in ['e', 'E']:
            self.p += 1
            if self.p > len(s) - 1:
                return False
            number = number and self.scanInterger(s)

        if self.p < len(s):
            return False

        return number

    def scanInterger(self, s):
        if s[self.p] in ['+', '-']:
            self.p += 1
        return self.scanUnsignedInterger(s)

    def scanUnsignedInterger(self, s):
        pre = self.p
        while (self.p < len(s) and s[self.p] >= '0' and s[self.p] <= '9'):
            self.p += 1
        return self.p > pre


# print(Solution().isNumber("1 "))
# print(Solution().isNumber("e9"))
print(Solution().isNumber("3.1416"))

