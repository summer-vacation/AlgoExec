# -*- coding: utf-8 -*-
"""

   File Name：     is_valid
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/901/

   有效的括号
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True
        if len(s)%2 == 1:
            return False
        res = [s[0]]
        index = 0
        for i in range(1, len(s)):
            char = s[i]
            if char == ")":
                if index >= 0 and res[index] == "(":
                    res.pop(index)
                    index -= 1
                else:
                    return False
            elif char == "}":
                if index >= 0 and res[index] == "{":
                    res.pop(index)
                    index -= 1
                else:
                    return False
            elif char == "]":
                if index >= 0 and res[index] == "[":
                    res.pop(index)
                    index -= 1
                else:
                    return False
            else:
                res.append(char)
                index += 1
        return True if index == -1 else False

    def isValid2(self, s: str) -> bool:
        map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in map:
                top = stack.pop() if stack else '#'
                if map[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == '__main__':
    print(Solution().isValid("(]"))


