# -*- coding: utf-8 -*-
"""

   File Name：     maxProfit02
   Author :       jing
   Date：          2020/3/20

   https://leetcode-cn.com/explore/interview/card/tencent/226/dynamic-programming/924/

   多次买卖一支股票

   即找出所有的递增子序列
"""


class Solution:
    def maxProfit(self, prices) -> int:
        if prices is None or len(prices) < 2:
            return 0
        all_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                all_profit += (prices[i] - prices[i - 1])       # 所有增量的和
        return all_profit

