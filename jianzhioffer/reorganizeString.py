# -*- coding: utf-8 -*-
"""
File Name:    reorganizeString.py
Author :      jynnezhang
Date:         2020/6/8 8:46 下午
Description:
"""


class Solution:
    def reorganizeString(self, S: str) -> str:
        if S is None or len(S) == 0:
            return ""
        pre, last = 1, 0
        while pre < len(S):
            if S[pre] != S[last]:

                if pre < len(S) and pre - last >= 2:
                    last += 1
                    print(S[:last], S[pre], S[last+1:pre], S[pre+1:])
                    S = S[:last] + S[pre] + S[last+1:pre] + S[last] + S[pre+1:]
                    pre += 1
                    last += 1
            else:
                pre += 1

        return "" if (pre - last == 1 and S[pre] == S[last]) or pre - last > 2 else S


if __name__ == '__main__':
    print(Solution().reorganizeString("vvvlo"))
