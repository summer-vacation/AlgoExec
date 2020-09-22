# -*- coding: utf-8 -*-
"""
File Name:    longestSubstring.py
Author :      jynnezhang
Date:         2020/9/22 9:30 下午
Description:

至少有K个重复字符的最长子串
https://leetcode-cn.com/leetbook/read/top-interview-questions/xafdmc/
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s) or k == 0 or len(s) == 0:
            return 0

        return self.getLongest(s, k)

    def getLongest(self, s, k):
        if k > len(s):
            return 0
        count = {}
        for c in s:
            if c in count.keys():
                count[c] += 1
            else:
                count[c] = 1
        # 起点、终点向中间靠拢，去掉首位不符合条件的字符串(滑动窗口) -> 不合符要求：出现次数小于k
        start, end = 0, len(s)-1
        while start <= end and count[s[start]] < k < len(s):
            start += 1
        while end >= start and count[s[end]] < k < len(s):
            end -= 1
        # 字符串中间存在不符合条件的字符，即以该字符串为界，分割前子串和后字串，进行计算(分治)
        for i in range(start, end+1):
            if count[s[i]] < k:
                return max(self.getLongest(s[start:i], k), self.getLongest(s[i+1:end+1], k))
        return end - start + 1


if __name__ == '__main__':
    print(Solution().longestSubstring("weitong", 2))
