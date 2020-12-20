# -*- coding: utf-8 -*-
"""
File Name:    group-anagrams.py
Author :      jynnezhang
Date:         2020/12/14 7:35 下午
Description:
https://leetcode-cn.com/problems/group-anagrams/
"""
import collections


class Solution:
    def groupAnagrams(self, strs):
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
