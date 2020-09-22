# -*- coding: utf-8 -*-
"""

   File Name：     addTwoNumbers
   Author :       jing
   Date：          2020/3/18
   https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/909/

   两数相加
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

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return None
        len_l1, len_l2 = 0, 0
        tmp_l1, tmp_l2 = l1, l2
        while tmp_l1:
            tmp_l1 = tmp_l1.next
            len_l1 += 1
        while tmp_l2:
            tmp_l2 = tmp_l2.next
            len_l2 += 1
        if len_l1 < len_l2:
            l1, l2 = l2, l1
        up = 0
        head = ListNode(0)
        i = 0
        while l2:
            res = l1.val + l2.val + up
            up = 0
            if res >= 10:
                up, cur = divmod(res, 10)
            else:
                cur = res
            if i == 0:
                result = ListNode(cur)
                head.next = result
                i += 1
            else:
                result.next = ListNode(cur)
                result = result.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            res = l1.val + up
            up = 0
            up, cur = divmod(res, 10)
            result.next = ListNode(cur)
            result = result.next
            l1 = l1.next
        if up != 0:
            result.next = ListNode(up)
        return head.next


if __name__ == '__main__':
    root = ListNode(1)
    # root.next = ListNode(4)
    # root.next.next = ListNode(3)

    root2 = ListNode(9)
    root2.next = ListNode(9)
    # root2.next.next = ListNode(4)
    print(Solution().addTwoNumbers2(root, root2))
