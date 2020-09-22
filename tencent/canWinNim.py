# -*- coding: utf-8 -*-
"""

   File Name：     canWinNim
   Author :       jing
   Date：          2020/3/25

   https://leetcode-cn.com/problems/nim-game/

   Nim游戏
"""


class Solution:
    # 赢的要点就是，在你的对手最后一次拿的时候，石头要是4个， 这时无论他拿1、2、3个，你都有石头拿。
    # 要保证这一点，你需要保证每次你拿完时石头的个数是4的倍数。那就意味着一开始石头的数目不是4的倍数。
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        return True


l = [1, 2, 3]
print(l.pop(0))
print(l)
