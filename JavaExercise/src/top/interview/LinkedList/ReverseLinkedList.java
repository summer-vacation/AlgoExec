package top.interview.LinkedList;

public class ReverseLinkedList {

    /**
     * 反转
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

    public static void main(String[] args) {
        ListNode root = new ListNode(1);
        root.next = new ListNode(2);
        root.next.next = new ListNode(3);
        root.next.next.next = new ListNode(4);
        root.next.next.next.next = new ListNode(5);
        new ReverseLinkedList().reverseList(root);
    }
}
