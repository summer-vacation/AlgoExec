# -*- coding: utf-8 -*-
"""

   File Name：     topKFrequent
   Author :       jing
   Date：          2020/4/7
"""
import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        from collections import Counter
        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[3,0,1,0], k = 1))
