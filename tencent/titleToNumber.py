# -*- coding: utf-8 -*-
"""

   File Name：     titleToNumber
   Author :       jing
   Date：          2020/4/12

   https://leetcode-cn.com/interview/0/submissions/
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        mapper = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,'J': 10,'K': 11, 'L': 12,'M': 13,'N': 14,'O': 15,'P': 16,'Q': 17,'R': 18,'S': 19,'T': 20,'U': 21,'V': 22,'W': 23,'X': 24,'Y': 25,'Z': 26}
        index = 1
        result = 0
        for c in s[::-1]:
            result += pow(26, index-1) * mapper[c]
            index += 1
        return result
