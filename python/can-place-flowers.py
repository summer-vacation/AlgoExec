# -*- coding: utf-8 -*-
"""
File Name:    can-place-flowers.py
Author :      jynnezhang
Date:         2020/11/17 1:48 下午
Description:
https://leetcode-cn.com/problems/can-place-flowers
"""


class Solution:
    # todo
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        str_flowerbed = ''.join(map(str, flowerbed))
        flowerbed_list = str_flowerbed.split('1')
        first = False if flowerbed[0] == 1 else True
        end = False if flowerbed[0] == 1 else True
        if len(flowerbed_list) == 1:
            if not first and not end:
                return True if n == 0 else False

        for index, l in flowerbed_list:
            pass

if __name__ == '__main__':
    print(Solution().canPlaceFlowers(flowerbed = [1,0,0,1], n =1))
