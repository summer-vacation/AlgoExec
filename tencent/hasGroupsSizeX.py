# -*- coding: utf-8 -*-
"""

   File Name：     hasGroupsSizeX
   Author :       jing
   Date：          2020/3/27

   https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/

   卡牌分组
"""


class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        if deck is None or len(deck) == 0:
            return False
        import collections
        len_deck = len(deck)
        count = collections.Counter(deck)
        for X in range(2, len_deck+1):
            if len_deck % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False
