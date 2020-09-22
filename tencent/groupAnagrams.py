# -*- coding: utf-8 -*-
"""

   File Name：     groupAnagrams
   Author :       jing
   Date：          2020/4/10

   https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/77/
"""


class Solution:
    def groupAnagrams(self, strs):
        if strs is None or len(strs) == 0:
            return []
        res = []
        if len(strs) == 1:
            res.append(strs)
            return res

        hashMap = {}
        for s in strs:
            if s == "":
                if s not in hashMap.keys():
                    hashMap[s] = [""]
                else:
                    hashMap[s].append(s)
                continue
            # lambda x: (x.sort(), x)[1] 相当于一个函数，(list(s))相当于传进参数
            # lambda表达式，返回x.sort(), x, [1]第一个结果取x, 即排序之后的值
            sort_s = "".join((lambda x: (x.sort(), x)[1])(list(s)))
            if sort_s not in hashMap.keys():
                hashMap[sort_s] = []
            hashMap[sort_s].append(s)

        for value in hashMap.values():
            res.append(value)
        return res


print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

x = "321"
s = "string"
print((lambda x: (x.sort(), x)[1])([3, 2, 1]))
