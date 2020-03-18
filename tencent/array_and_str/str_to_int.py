# -*- coding: utf-8 -*-
"""

   File Name：     str_to_int
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/897/
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        if str is None:
            return 0
        str = str.strip()
        if str == "" or len(str) == 0:
            return 0
        result = ""
        if str[0] == "-" or str[0] == "+":
            result = result + str[0]
            str = str[1:]
        elif not str[0].isdigit():
            return 0
        for char in str:
            if char.isdigit():
                result = result + char
            else:
                break
        # 考虑输入为"+" "-"时
        if result == "+" or result == "-":
            return 0
        result = int(result)
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        elif result < - 2 ** 31:
            result = - 2 ** 31
        return int(result)

    def myAtoi2(self, str: str) -> int:
        import re

        pattern = r"[\s]*[+-]?[\d]+"
        match = re.match(pattern, str)
        if match:
            res = int(match.group(0))
            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            if res < - 2 ** 31:
                res = - 2 ** 31
        else:
            res = 0
        return res


if __name__ == '__main__':
    print(int("+1234"))
    print(Solution().myAtoi("     -42+123"))




