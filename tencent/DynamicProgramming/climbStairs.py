# -*- coding: utf-8 -*-
"""

   File Name：     climbStairs
   Author :       jing
   Date：          2020/3/20

   https://leetcode-cn.com/explore/interview/card/tencent/226/dynamic-programming/921/

   爬楼梯
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        result = []
        i = 0
        while i <= 2:
            result.append(i)
            i += 1

        for i in range(3, n+1):
            result.append(result[i-2] + result[i-1])   # 状态转移方程： 要么跨一步到n,要么2步，所以是result[i-2] + result[i-1]

        return result[n]


if __name__ == '__main__':
    print(Solution().climbStairs(4))



