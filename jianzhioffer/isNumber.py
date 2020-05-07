# -*- coding: utf-8 -*-
"""

   File Name：     isNumber
   Author :       jing
   Date：          2020/4/13

   https://leetcode-cn.com/problems/valid-number/

   表示数值的字符串

   串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，
   但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        sign, decimal, hasE = False, False, False
        for i in range(0, len(s)):
            if s[i] in ['e', 'E']:
                if i == len(s) - 1 or hasE:
                    return False
                hasE = True
            elif s[i] == '.':
                if hasE or decimal:
                    return False
                decimal = True
            elif s[i] in ['+', '-']:
                if not sign and i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
                if sign and s[i - 1] not in ['e', 'E']:
                    return False
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True


print(Solution().isNumber("5e2"))
