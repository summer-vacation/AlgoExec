# -*- coding: utf-8 -*-
"""

   File Name：     translateNum
   Author :       jing
   Date：          2020/4/26

   把数字翻译成字符串，求不同的翻译个数
"""


class Solution:
    def translateNum(self, num: int) -> int:
        if num is None or num < 0:
            return 0
        if 0 <= num <= 9:
            return 1
        mod = num % 100
        if mod <= 9 or mod >= 26:
            return self.translateNum(num // 10)
        else:
            return self.translateNum(num // 100) + self.translateNum(num // 10)


print(Solution().translateNum(12258))
