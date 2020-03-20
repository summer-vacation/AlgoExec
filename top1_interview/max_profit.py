# -*- coding: utf-8 -*-
"""

   File Name：     max_profit
   Author :       jing
   Date：          2019-12-08
   https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
   找到所有连续递增的子序列
"""


class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        submin = 0
        for i in range(1, len(prices)):
            if prices[i-1] <= prices[i]:
                if i == len(prices) - 1:
                    profit = profit + (prices[i] - prices[submin])
                continue
            else:
                 profit = profit + (prices[i-1] - prices[submin])
                 submin = i
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([1, 5, 5, 6, 4, 10]))
