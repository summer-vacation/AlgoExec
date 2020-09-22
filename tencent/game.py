# -*- coding: utf-8 -*-
"""

   File Name：     game
   Author :       jing
   Date：          2020/4/3

   猜数字

   https://leetcode-cn.com/problems/guess-numbers/
"""


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum([guess[i] == answer[i] for i in range(len(guess))])

    def game2(self, guess: List[int], answer: List[int]) -> int:
        if guess is None or len(guess) == 0 or answer is None or len(answer) == 0:
            return 0
        res = 0
        for i in range(3):
            if guess[i] == answer[i]:
                res += 1
        return res
