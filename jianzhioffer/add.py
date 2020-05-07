# -*- coding: utf-8 -*-
"""
File Name:    add.py
Author :      jynnezhang
Date:         2020/5/1 10:46 上午
Description:

不使用运算符号，完成加法

不用加减乘除做加法

https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/

java:

class Solution {
    public int add(int a, int b) {
        while(b != 0) { // 当进位为 0 时跳出
            int c = (a & b) << 1;  // c = 进位
            a ^= b; // a = 非进位和
            b = c; // b = 进位
        }
        return a;
    }
}

"""


class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff      # 4*8  32位
        a, b = a & x, b & x     # 与，全1则1
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x        # a ^ b：相异为1，
            # a = a ^ b
            # b = (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


print(Solution().add(1, 13))
