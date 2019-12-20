package top.interview.LinkedList;

public class MergeTwoSortedLists {

    /**
     * https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/771/
     * @param l1
     * @param l2
     * @return
     */
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        merge(l1, l2, result);
        return result.next;
    }

    private void merge(ListNode l1, ListNode l2, ListNode result) {
        if (l1 == null && l2 == null) {
            return;
        } else if (l1 != null && l2 == null) {
            result.next = l1;
            return;
        } else if (l1 == null && l2 != null) {
            result.next = l2;
            return;
        } else {
            if (l1.val <= l2.val) {
                result.next = l1;
                merge(l1.next, l2, result.next);
            } else {
                result.next = l2;
                merge(l1, l2.next, result.next);
            }
        }
    }

    public static void main(String[] args) {
        ListNode root = new ListNode(1);
        root.next = new ListNode(2);
        root.next.next = new ListNode(4);
//        root.next.next.next = new ListNode(4);
//        root.next.next.next.next = new ListNode(5);
        ListNode root2 = new ListNode(1);
        root2.next = new ListNode(3);
        root2.next.next = new ListNode(4);
        new MergeTwoSortedLists().mergeTwoLists(root, root2);
    }
}
