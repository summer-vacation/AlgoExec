# -*- coding: utf-8 -*-
"""

   File Name：     addTwoNumbers
   Author :       jing
   Date：          2020/3/18
   https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/909/
"""

from tencent.linkedlist.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        pre = result = ListNode(0)
        pl = 0
        while l1 is not None:
            if l2 is not None:
                temp = l1.val + l2.val
                l2 = l2.next
            else:
                temp = l1.val
            div, mod = divmod(temp+pl, 10)
            result.next = ListNode(mod)
            pl = div
            l1 = l1.next
            result = result.next
        while l2 is not None:
            div, mod = divmod(l2.val+pl, 10)
            result.next = ListNode(mod)
            pl = div
            l2 = l2.next
            result = result.next
        if pl != 0:
            result.next = ListNode(pl)

        return pre.next


if __name__ == '__main__':
    root = ListNode(9)
    root.next = ListNode(9)
    # root.next.next = ListNode(3)

    root2 = ListNode(9)
    # root2.next = ListNode(9)
    # root2.next.next = ListNode(4)
    print(Solution().addTwoNumbers(root, root2))
