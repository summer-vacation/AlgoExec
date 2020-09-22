# -*- coding: utf-8 -*-
"""

   File Name：     removeVowels
   Author :       jing
   Date：          2020/4/3


"""


class Solution:
    def removeVowels(self, S: str) -> str:
        return ''.join(filter(lambda c: c not in 'aeiou', S))
