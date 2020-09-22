# -*- coding: utf-8 -*-
"""

   File Name：     reverseBits
   Author :       jing
   Date：          2020/3/24
https://leetcode-cn.com/problems/reverse-bits/
   颠倒二进制位
"""


class Solution:
    # bin(n)：将十进制数转换为二进制字符串，不过字符串首段有“0b”字符；
    # s.rjust(32, '0')：将字符串s补全为长度为32的字符串，s右对齐，不够的地方用字符“0”补全；
    # int(x, base=2)：将二进制字符串转换为十进制数
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].rjust(32, '0')[::-1], base=2)


print(Solution().reverseBits(43261596))

