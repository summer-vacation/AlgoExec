# -*- coding: utf-8 -*-
"""

   File Name：     longest_palindrome
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/896/
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ""
        result = s[0]
        max_len = 1
        lens = len(s)
        for i in range(lens):
            j = i+1
            while j < lens:
                pp = s[i:j+1]
                if pp == pp[::-1]:
                    if j + 1 - i > max_len:
                        max_len = j - i
                        result = pp
                j += 1
        return result

    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        max_len = 1
        start = 0
        for i in range(1,n):
            even = s[i-max_len:i+1]
            odd = s[i-max_len-1:i+1]
            if i-max_len-1 >= 0 and odd == odd[::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            if i-max_len >= 0 and even == even[::-1]:
                start = i-max_len
                max_len += 1
        return s[start:start+max_len]

    def longestPalindrome3(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ""
        if len(s) == 1 or self.isPalindrome(s):
            return s
        start, end = 0, 0
        max_len = 0
        result = None
        while start < len(s):
            end = start
            while end < len(s):
                if self.isPalindrome(s[start:end+1]):
                    if max_len < end-start+1:
                        result = s[start:end+1]
                        max_len = end-start+1
                end = end + 1
            start += 1
        return result

    def isPalindrome(self, inputs):
        return inputs == inputs[::-1]


if __name__ == '__main__':
    print(Solution().longestPalindrome3("ac"))
