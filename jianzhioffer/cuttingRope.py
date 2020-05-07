# -*- coding: utf-8 -*-
"""

   File Name：     cuttingRope
   Author :       jing
   Date：          2020/4/26

   剪绳子，chang'du
"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        # write code here
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
            # 申请辅助空间
        products = [0 for i in range(n+1)]
        # 定义前几个初始变量的值, 为什么这样定？
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        # 进行动态规划,也就是从下向上的进行求解
        for i in range(4, n + 1):
            max_ = 0
            for j in range(1, i // 2 + 1):
                max_ = max(products[j] * products[i - j], max_)
            products[i] = max_

        return products[n] % 1000000007


print(Solution().cuttingRope(8))
