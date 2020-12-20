# -*- coding: utf-8 -*-
"""
File Name:    best-time-to-buy-and-sell-stock-with-transaction-fee.py
Author :      jynnezhang
Date:         2020/12/17 1:40 下午
Description:
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润，
dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润（i 从 0 开始）
"""


class Solution:
    def maxProfit(self, prices=[], fee=0) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

    def maxProfit2(self, prices=[], fee=0) -> int:
        n = len(prices)
        sell, not_sell = 0, -prices[0]
        for i in range(1, n):
            temp = sell
            sell = max(sell, not_sell + prices[i] - fee)
            not_sell = max(not_sell, temp - prices[i])
        return sell


if __name__ == '__main__':
    print(Solution().maxProfit2(prices=[1, 3, 2, 8, 4, 9], fee=2))


