# -*- coding: utf-8 -*-
"""
File Name:    backspace-string-compare.py
Author :      jynnezhang
Date:         2020/10/19 3:43 下午
Description:
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = S.lstrip("#")
        T = T.lstrip("#")
        while "#" in S:
            index = S.index("#")
            if index < len(S):
                S = S[:index-1] + S[index+1:]
            else:
                S = S[:index-1]
            S = S.lstrip("#")
        while "#" in T:
            index = T.index("#")
            if index < len(T):
                T = T[:index-1] + T[index+1:]
            else:
                T = T[:index-1]
            T = T.lstrip("#")
        print(S)
        print(T)
        return True if S == T else False


if __name__ == '__main__':
    print(Solution().backspaceCompare(S = "a##c", T = "#a#c"))

