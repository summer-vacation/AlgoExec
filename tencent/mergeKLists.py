
# -*- coding: utf-8 -*-
"""

   File Name：     mergeKLists
   Author :       jing
   Date：          2020/4/26

   合并K个有序链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 第一种方法：先合并所有的元素，然后再进行排序
    def mergeKLists_01(self, lists) -> ListNode:
        if lists is None or len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]
        # 遍历链表，将所有链表的所有元素放到一个数组里面
        nodeList = []
        for i in range(len(lists)):
            currentNode = lists[i]
            # 遍历某个链表
            while (currentNode):
                nodeList.append(currentNode)
                currentNode = currentNode.next

        # 根据node的val对数组进行排序
        nodeList = sorted(nodeList, key=lambda x: x.val)

        # 对排序好的数组的元素，一个个地连接成新的链表（这里的tempHead是为了方便设置的头节点）
        tempHead = ListNode(0)
        currentNode = tempHead
        for i in range(len(nodeList)):
            currentNode.next = nodeList[i]
            currentNode = currentNode.next

        return tempHead.next

    # 对lists里面的链表两两合并，直到lists里面只有一个元素
    def mergeKLists_02(self, lists) -> ListNode:
        if lists is None or len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]
        while len(lists) > 1:
            list1 = lists.pop()
            list2 = lists.pop()
            lists.append(self.mergeTowLists(list1, list2))
        return lists[0]

    def mergeTowLists(self, list1, list2):
        head = None
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            head = list1
            head.next = self.mergeTowLists(list1.next, list2)
        else:
            head = list2
            head.next = self.mergeTowLists(list, list2.next)
        return head

    # 对lists里面的链表两两合并，二分归并
    def mergeKLists_03(self, lists) -> ListNode:
        if lists is None or len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]
        return self.partition(lists, 0, len(lists) - 1)

    def partition(self, lists, start, end):
        if start == end:
            return lists[start]
        if start < end:
            mid = (start + end) // 2
            l1 = self.partition(lists, start, mid)
            l2 = self.partition(lists, mid + 1, end)
            return self.mergeTowLists_03(l1, l2)

    def mergeTowLists_03(self, list1, list2):
        head = None
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            head = list1
            head.next = self.mergeTowLists(list1.next, list2)
        else:
            head = list2
            head.next = self.mergeTowLists(list1, list2.next)
        return head
