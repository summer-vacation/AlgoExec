# -*- coding: utf-8 -*-
"""

   File Name：     longestStrChain
   Author :       jing
   Date：          2020/4/2

   最长字符串链  ---   longestStrChain
   输入：["a","b","ba","bca","bda","bdca"]
    输出：4
    解释：最长单词链之一为 "a","ba","bda","bdca"。
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if words is None or len(words) == 0:
            return 0
        words = sorted(words, key=lambda x: len(x))
        dp = [1 for _ in range(len(words))]
        for i, word in enumerate(words):
            if i >= 1 and words[i] == words[i - 1]:  # 去重
                continue
            for j in range(i + 1, len(words)):
                if len(words[j]) == len(word):  # 长度相等不考虑
                    continue
                if len(words[j]) - 1 > len(word):  # 长度差超过1也不考虑
                    break
                if len(words[j]) - 1 == len(word) and self.canTransfer(word, words[j]):
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

    def canTransfer(self, str1, str2):
        tmp = ""
        for i, char in enumerate(str2):
            tmp = str2[:i] + str2[i + 1:]
            if tmp == str1:
                return True
        return False


print(Solution().canTransfer(["a","b","ba","bca","bda","bdca"]))
