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
            if i-max_len-1>=0 and odd == odd[::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            if i-max_len>=0 and even == even[::-1]:
                start = i-max_len
                max_len += 1
        return s[start:start+max_len]


if __name__ == '__main__':
    print(Solution().longestPalindrome2("abb"))
