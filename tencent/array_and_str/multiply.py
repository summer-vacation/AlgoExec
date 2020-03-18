# -*- coding: utf-8 -*-
"""

   File Name：     multiply
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/904/
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"
        return str(eval(num1+'*'+num2))


if __name__ == '__main__':
    print(2**31-1)
    print(Solution().multiply(num1 = "123", num2 = "456"))
