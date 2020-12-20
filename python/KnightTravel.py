# -*- coding: utf-8 -*-
"""
File Name:    KnightTravel.py
Author :      jynnezhang
Date:         2020/11/5 10:12 下午
Description:
"""


class KnightTravel():
    def Travel(self, start, end):
        uset = set()
        v = {}

        v[start / 8] = start % 8
        uset.add(start)
        level = 0
        while v is not None or len(v) != 0:
            t = {}
            for key, value in v:
                if key * 8 + value == end:
                    return level
                uset.add(key * 8 + value)
                if key - 2 >= 0 and value - 1 >= 0 and uset[(key - 2) * 8 + value - 1] == uset[len(uset)-1]:
                    t[key - 2] =  value - 1
                    uset.add((key - 2) * 8 + value - 1)
