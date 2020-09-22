# -*- coding: utf-8 -*-
"""

   File Name：     longestValidParentheses
   Author :       jing
   Date：          2020/3/30

    最长有效括号
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        map = {')': '(', ']': '[', '}': '{'}
        stack = []
        res = 0
        for char in s:
            if char in map.keys():
                if stack:
                    top = stack.pop()
                else:
                    top = '#'
                if map[char] != top:
                    continue
                else:
                    res += 2
            else:
                stack.append(char)
        return res


print(Solution().longestValidParentheses("((())"))
