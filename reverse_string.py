# -*- coding: utf-8 -*-
"""

   File Name：     reverse_string
   Author :       jing
   Date：          2019-11-26
   反转字符串，使用 O(1) 的额外空间
   https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/275/string/1144/
"""


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        if s is None:
            return None
        else:
            return s.reverse()

"""
第一种：使用字符串切片
result = s[::-1]
第二种：使用列表的reverse方法
l = list(s)
l.reverse()
result = "".join(l)

# l = list(s)
# result = "".join(l[::-1])
第三种：使用reduce
result = reduce(lambda x,y:y+x,s)
第四种：使用递归函数
def func(s):
    if len(s) <1:
        return s
    return func(s[1:])+s[0]
result = func(s)
第五种：使用栈
def func(s):
    l = list(s) #模拟全部入栈
    result = ""
    while len(l)>0:
        result += l.pop() #模拟出栈
    return result
result = func(s)
第六种：for循环
def func(s):
    result = ""
    max_index = len(s)-1
    for index,value in enumerate(s):
        result += s[max_index-index]
    return result
result = func(s)
"""


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)

