package top.interview.LinkedList;

public class RemoveNthNodeFromEndofList {
    /**
     * 双指针，一个先跑，另一个间隔n再跑
     * https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
     * @param head
     * @param n
     * @return
     */
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null) {
            return null;
        }
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode pre1 = dummyHead, pre2 = dummyHead;
//        for (int i = 0; i <= n; i++){
//            pre1 = pre1.next;
//        }
        int j = 0;
        while (pre1 != null){
            pre1 = pre1.next;
            if (j > n) {
                pre2 = pre2.next;
            }else{
                j++;
            }
        }
        pre2.next = pre2.next.next;
        return dummyHead.next;
    }

    public static void main(String[] args) {
        ListNode root = new ListNode(1);
        root.next = new ListNode(2);
//        root.next.next = new ListNode(3);
//        root.next.next.next = new ListNode(4);
//        root.next.next.next.next = new ListNode(5);
        new RemoveNthNodeFromEndofList().removeNthFromEnd(root, 2);
    }
}
