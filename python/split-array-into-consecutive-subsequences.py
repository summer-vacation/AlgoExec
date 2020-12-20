# -*- coding: utf-8 -*-
"""
File Name:    split-array-into-consecutive-subsequences.py
Author :      jynnezhang
Date:         2020/12/4 2:19 下午
Description:
https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/
"""
import collections
import heapq


class Solution:
    def isPossible(self, nums=[]) -> bool:
        if not nums or len(nums) < 3:
            return False
        mp = collections.defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)

        return not any(queue and queue[0] < 3 for queue in mp.values())


if __name__ == '__main__':
    print(Solution().isPossible([1,2,3,3,4,5]))
