# -*- coding: utf-8 -*-
"""

   File Name：     max_len_strs
   Author :       jing
   Date：          2020/4/13

   两个字符串的最长公共子串
"""


def max_len_substrs(string1, string2):
    if string1 is None or string2 is None or len(string1) == 0 or len(string2) == 0:
        return ""
    len1 = len(string1)
    len2 = len(string2)

    dp = [[0 for i in range(len2+1)] for j in range(len1+1)]
    max_len = 0
    end = 0
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if max_len < dp[i][j]:
                max_len = dp[i][j]
                end = i

    return string1[end-max_len: end]


print(max_len_substrs("wqabc", "abcdec"))
print(max_len_substrs("", ""))
print(max_len_substrs("wqabc", "aw"))
print(max_len_substrs("www", "wwq"))
print(max_len_substrs("abc", "def"))
print(max_len_substrs("bfwehfbwehcwekfv1231csd", "defbwehcw"))

