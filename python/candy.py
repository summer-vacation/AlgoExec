# -*- coding: utf-8 -*-
"""
File Name:    candy.py
Author :      jynnezhang
Date:         2020/11/16 12:30 下午
Description:
https://leetcode-cn.com/problems/candy/
"""


class Solution:
    def candy(self, ratings):
        if ratings is None:
            return 0
        if len(ratings) == 1:
            return 1
        nums = len(ratings)
        candies = [1 for i in range(nums)]
        for i in range(1, nums):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for j in range(nums-1, 0, -1):
            if ratings[j-1] > ratings[j] and candies[j-1] <= candies[j]:
                candies[j-1] = candies[j] + 1

        return sum(candies)


if __name__ == '__main__':
    print(Solution().candy([1,2,87,87,87,2,1]))
