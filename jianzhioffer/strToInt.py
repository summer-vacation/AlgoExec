# -*- coding: utf-8 -*-
"""

   File Name：     strToInt
   Author :       jing
   Date：          2020/4/13

   https://leetcode-cn.com/problems/string-to-integer-atoi/
"""


class Solution:
    def strToInt(self, str: str) -> int:
        import re
        match = re.match(r"[\s]*[+-]?[\d]+", str)
        if match:
            res = int(match.group(0))
            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            if res < - 2 ** 31:
                res = - 2 ** 31
        else:
            res = 0
        return res


print(Solution().strToInt(" -987"))
