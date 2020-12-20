# -*- coding: utf-8 -*-
"""
File Name:    word-pattern.py
Author :      jynnezhang
Date:         2020/12/16 9:26 下午
Description:

https://leetcode-cn.com/problems/word-pattern/
"""
import collections


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False

        for index, c in enumerate(pattern):
            if (c in ch2word and ch2word[c] != words[index]) \
                    or (words[index] in word2ch and word2ch[words[index]] != c):
                print(c, ch2word[c], words[index], word2ch[words[index]])
                return False
            word2ch[words[index]] = c
            ch2word[c] = words[index]

        return True


if __name__ == '__main__':
    print(Solution().wordPattern('abba', 'dog cat cat dog'))
