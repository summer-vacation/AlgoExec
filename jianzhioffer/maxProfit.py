# -*- coding: utf-8 -*-
"""

   File Name：     maxProfit
   Author :       jing
   Date：          2020/4/13

    股票的最大利润

    只交易一次
"""


class Solution:
    def maxProfit(self, prices) -> int:
        if prices is None or len(prices) < 2:
            return 0

        min_p = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            pp = prices[i]
            if pp < min_p:
                min_p = pp
            else:
                max_profit = max(pp - min_p, max_profit)

        return max_profit


print(Solution().maxProfit([7,1,5,3,6,4]))
