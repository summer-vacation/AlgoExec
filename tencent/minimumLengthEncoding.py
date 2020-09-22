# -*- coding: utf-8 -*-
"""

   File Name：     minimumLengthEncoding
   Author :       jing
   Date：          2020/3/28
"""


class Solution:
    def minimumLengthEncoding(self, words) -> int:
        if words is None or len(words) == 0:
            return 0

        result = 0
        word_map = {}
        for word in words:
            for i in range(len(word), 0, -1):
                key = word[i-1:][::-1]
                if key in word_map.keys():
                    if word_map[key] == 99:
                        result = result - len(key) - 1
                    continue
                else:
                    if i == 1:
                        word_map[key] = 99
                        result = result + len(word) + 1
                    else:
                        word_map[key] = 0
        return result

    def minimumLengthEncoding2(self, words: List[str]) -> int:
        if words is None or len(words) == 0:
            return 0

        result = 0
        word_m = set(words)
        for word in words:
            for i in range(1, len(word)):
                word_m.discard(word[i:])
        for word in word_m:
            result = result + len(word) + 1
        return result


# print(Solution().minimumLengthEncoding(["time", "me", "bell"]))
print(Solution().minimumLengthEncoding(["me", "time"]))
sr = "12"
