# -*- coding: utf-8 -*-
"""
File Name:    swapNumbers.py
Author :      jynnezhang
Date:         2020/9/29 11:09 下午
Description:

https://leetcode-cn.com/problems/swap-numbers-lcci/

不用变量交换2个数字
"""


class Solution:
    def swapNumbers(self, numbers):
        """
        使用加法：
        a = a + b   --->  c
        b = a - b   --->  a
        a = a - b   --->  b
        :param numbers:
        :return:
        """
        if numbers is None or len(numbers) < 2:
            return None
        numbers[0] = numbers[0] + numbers[1]
        numbers[1] = numbers[0] - numbers[1]
        numbers[0] = numbers[0] - numbers[1]
        return numbers

    def swapNumbers2(self, numbers):
        """
        使用异或：
        a = a ^ b   --->  c
        b = a ^ b   --->  a^b^b  ---> a
        a = a ^ b   --->  a^b^a  ---> b
        :param numbers:
        :return:
        """
        if numbers is None or len(numbers) < 2:
            return None
        numbers[0] = numbers[0] ^ numbers[1]
        numbers[1] = numbers[0] ^ numbers[1]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers
