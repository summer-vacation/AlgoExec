# -*- coding: utf-8 -*-
"""
File Name:    find-the-longest-substring-containing-vowels-in-even-counts.py
Author :      jynnezhang
Date:         2020/11/13 3:20 下午
Description:
https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                sub = s[j:j + i]
                has_odd_vowel = False
                for vowel in ['a', 'e', 'i', 'o', 'u']:
                    if sub.count(vowel) % 2 != 0:
                        has_odd_vowel = True
                        break
                if not has_odd_vowel: return i
        return 0

    def findTheLongestSubstring2(self, s: str) -> int:
        mapper = {
            "a": 1,
            "e": 2,
            "i": 4,
            "o": 8,
            "u": 16
        }
        seen = {0: -1}
        res = cur = 0

        for i, c in enumerate(s):
            if c in mapper:
                cur ^= mapper.get(c)
                # 全部奇偶性都相同，相减一定都是偶数
            if cur in seen:
                # cur==0，res+1    元音偶数个，非元音
                # cur!=0, max(之前最大，当前位置-上一次非偶数元音起点)
                res = max(res, i - seen.get(cur))
            else:
                seen[cur] = i
        return res


if __name__ == '__main__':
    print(Solution().findTheLongestSubstring2("eleetminicoworoep"))
