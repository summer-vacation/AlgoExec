# -*- coding: utf-8 -*-
"""
File Name:    validateStackSequences.py
Author :      jynnezhang
Date:         2020/4/28 5:03 下午
Description:

栈的压入、弹出序列

额外的stack存储
在pushed中找到与popped[i]相等的数，找到之前的所有入栈stack
对stack栈顶的树依次和popped[i]相比，如果相等，stack.pop()，i += 1

如果pushed遍历完后，stack为空，则说明popped序列没问题
否则，popped序列不存在
"""


class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)  # num 入栈
            while stack and stack[-1] == popped[i]:  # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack


print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
