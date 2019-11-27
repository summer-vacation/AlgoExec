# -*- coding: utf-8 -*-
"""

   File Name：     word_break
   Author :       jing
   Date：          2019-11-27
   单词拆分
"""


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if s in wordDict:
            return True
        else:
            for i in range(len(s)):
                t = s[:i+1]
                if t in wordDict:
                    if self.wordBreak(s[i+1:], wordDict):
                        return True
                else:
                    continue
            return False

    def wordBreak2(self, s: str, wordDict) -> bool:
        def find(start=0):
            if s[start:] in wordDict:
                return True
            for end in range(start, len(s)):
                sub_str = s[start:end + 1]
                if sub_str in wordDict:
                    if find(end + 1):
                        return True
            return False

        return find()


if __name__ == '__main__':
    # print(Solution().wordBreak("ab", ["a", "b"]))
    print(Solution().wordBreak("goalspecial", ["go", "goal", "goals", "special"]))
