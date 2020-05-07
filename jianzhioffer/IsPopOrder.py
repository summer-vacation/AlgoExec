# -*- coding: utf-8 -*-
"""

   File Name：     IsPopOrder
   Author :       jing
   Date：          2020/3/23
   https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

   栈的压入、弹出
"""

class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        if not pushV or len(pushV) != len(popV):
            return False
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True


if __name__ == '__main__':
    print(Solution().IsPopOrder())
