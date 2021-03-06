package top.interview.LinkedList;

public class ReverseLinkedList {

    /**
     * 反转
     * https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
     * @param head
     * @return
     */

    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode pre = null;
        ListNode cur = head;
        while (cur != null){
            ListNode temp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = temp;
        }
        return pre;
    }

    public ListNode reverseList_re(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode r = reverseList_re(head.next);
        head.next.next = head;
        head.next = null;
        return r;
    }

    public static void main(String[] args) {
        ListNode root = new ListNode(1);
        root.next = new ListNode(2);
        root.next.next = new ListNode(3);
        root.next.next.next = new ListNode(4);
        root.next.next.next.next = new ListNode(5);
        new ReverseLinkedList().reverseList_re(root);
    }
}
