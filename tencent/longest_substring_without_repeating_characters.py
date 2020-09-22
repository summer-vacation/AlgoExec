# -*- coding: utf-8 -*-
"""

   File Name：     longest_substring_without_repeating_characters
   Author :       jing
   Date：          2020/3/16

    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    最长不含重复字符的子字符串
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        temp = []
        lens = 0
        for char in s:
            if char not in temp:
                lens += 1
                temp.append(char)
            else:
                temp.append(char)
                temp = temp[temp.index(char)+1:]
                lens = len(temp)
            max_len = max(max_len, lens)
        return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("bcbdf"))

