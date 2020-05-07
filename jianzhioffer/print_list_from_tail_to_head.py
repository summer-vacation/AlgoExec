# -*- coding: utf-8 -*-
"""

   File Name：     print_list_from_tail_to_head
   Author :       jing
   Date：          2020/3/15
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

result = []

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # 压栈
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result

    # 递归
    def printListFromTailToHead2(self, listNode):
        if listNode is None:
            return
        self.printListFromTailToHead2(listNode.next)
        result.append(listNode.val)
        return result


if __name__ == '__main__':
    s = Solution()
    listNode = ListNode(67)
    listNode.next = ListNode(0)
    listNode.next.next = ListNode(24)
    listNode.next.next.next = ListNode(58)
    print(s.printListFromTailToHead2(listNode))
