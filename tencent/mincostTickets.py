# -*- coding: utf-8 -*-
"""
File Name:    mincostTickets.py
Author :      jynnezhang
Date:         2020/5/6 10:30 上午
Description:

最低票价
https://leetcode-cn.com/problems/minimum-cost-for-tickets/
"""


class Solution:
    def mincostTickets(self, days, costs) -> int:
        if days is None or len(days) == 0:
            return 0
        lens_d = len(days)
        dp = [float('inf') for i in range(days[lens_d - 1] + 1)]
        dp[0] = 0
        costs_d = [1, 7, 30]
        pre = dp[0]
        for i in range(1, days[lens_d - 1] + 1):
            if i not in days:
                dp[i] = pre
            else:
                for index, d in enumerate(costs_d):
                    if i >= d:
                        dp[i] = min(dp[i], dp[i - d] + costs[index])
                    else:
                        dp[i] = min(dp[i], dp[0] + costs[index])
                pre = dp[i]
        return dp[-1]

    def mincostTickets2(self, days, costs) -> int:
        dp = [0 for _ in range(days[-1] + 33)]  # 为了负数索引---------------33
        days_idx = 0  # 设定一个days指标，标记应该处理 days 数组中哪一个元素
        a, b, c = costs[0], costs[1], costs[2]
        size = days[-1] + 1
        start = days[0]

        for i in range(start, size):  # 万一6月1号之前不开学，我天天去学校，哈哈。优化
            # 不用集合，少了一次O(len(days))
            if i != days[days_idx]:  # 若当前天数不是待处理天数，则其花费费用和前一天相同
                dp[i] = dp[i - 1]
            else:
                # 若 i 走到了待处理天数，则从三种方式中选一个最小的
                dp[i] = min(dp[i - 1] + a,
                            dp[i - 7] + b,
                            dp[i - 30] + c)
                days_idx += 1
        return dp[days[-1]]  # 返回-------那天，就那天，


print(Solution().mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
print(Solution().mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]))
print(Solution().mincostTickets(days=[6, 8, 9, 18, 20, 21, 23, 25], costs=[2, 10, 41]))
