# -*- coding: utf-8 -*-
"""
File Name:    dota2-senate.py
Author :      jynnezhang
Date:         2020/12/11 7:09 下午
Description:
https://leetcode-cn.com/problems/dota2-senate/
"""
import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if not senate:
            return ''
        if len(senate) == 1:
            return 'Radiant' if senate[0] == 'R' else 'Dire'

        n = len(senate)
        mark_R = [i for i in range(n) if senate[i] == 'R']
        mark_D = [i for i in range(n) if senate[i] == 'D']

        while mark_D and mark_R:
            if mark_R[0] > mark_D[0]:
                mark_D.append(mark_D[0] + n)
            else:
                mark_R.append(mark_R[0] + n)
            mark_D.pop(0)
            mark_R.pop(0)
        return 'Radiant' if mark_R else 'Dire'


if __name__ == '__main__':
    print(Solution().predictPartyVictory('R'))
