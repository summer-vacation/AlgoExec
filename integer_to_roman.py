# -*- coding: utf-8 -*-
"""

   File Name：     integer_to_roman
   Author :       jing
   Date：          2020/3/17
   https://leetcode.com/problems/integer-to-roman/
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {1000: "M",
                  900: "CM",
                  500: "D",
                  400: "CD",
                  100: "C",
                  90: "XC",
                  50: "L",
                  40: "XL",
                  10: "X",
                  9: "IX",
                  5: "V",
                  4: "IV",
                  1: "I"}
        result = ""
        while num > 0:
            for k in symbol.keys():
                div, mod = divmod(num, k)
                if div > 0:
                    result = result + symbol[k] * div
                    num = mod
        return result


if __name__ == '__main__':
    print(Solution().intToRoman(58))
