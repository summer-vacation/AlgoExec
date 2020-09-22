# -*- coding: utf-8 -*-
"""

   File Name：     reverse_words
   Author :       jing
   Date：          2020/3/18

   https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/906/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s
        if " " not in s:
            return s[::-1]
        word_list = s.split(" ")
        result = ""
        for word in word_list:
            result = result + " " + word[::-1]
        return result.strip()

    def reverseWords2(self, s: str) -> str:
        return ' '.join(s.split(' ')[::-1])[::-1]


if __name__ == '__main__':
    print(Solution().reverseWords2("Let's take LeetCode contest"))
