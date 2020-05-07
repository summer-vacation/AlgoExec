# -*- coding: utf-8 -*-
"""

   File Name：     printNumbers
   Author :       jing
   Date：          2020/4/13

   https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof

   打印从1到最大的n位数
"""

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        if n == 0:
            return 0
        result = []
        index = 1
        while len(str(index)) <= n:
            result.append(index)
            index += 1
        return result


    def printNumbers2(self, n: int):
        if n == 0:
            return 0
        limit = pow(10, n)
        result = []
        for i in range(1, limit):
            result.append(i)

        return result
