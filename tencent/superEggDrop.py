# -*- coding: utf-8 -*-
"""

   File Name：     superEggDrop
   Author :       jing
   Date：          2020/4/12


"""


class Solution:
    def func(self, egg_nums, times):
        if egg_nums == 1:
            return times
        if times == 0:
            return 0
        else:
            return 1 + self.func(egg_nums, times - 1) + self.func(egg_nums - 1, times - 1)

    def superEggDrop(self, K: int, N: int) -> int:
        res = 1
        while self.func(K, res) < N:
            res += 1
        return res


print(Solution().superEggDrop(2, 6))
