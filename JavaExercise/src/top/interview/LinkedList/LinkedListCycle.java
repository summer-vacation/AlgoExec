package top.interview.LinkedList;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/773/
 * 判断链表是否有环
 * 1、如果没环，那么一定会有最后一个的next == null
 * 2、如果有环，那么一个快跑，一个慢跑，那么这两个一定会相遇
 * 剑指offer上的题
 */
public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        if (head == null){
            return false;
        }
        ListNode fast = head;
        ListNode slow = head;

        while(true){
            if (fast.next != null && fast.next.next != null) {
                fast = fast.next.next;
                slow = slow.next;
            }else {
                return false;
            }
            if (fast == slow){
                return true;
            }
        }
    }

    public static void main(String[] args) {
        ListNode input = new ListNode(1);
        input.next = new ListNode(2);
        input.next.next = new ListNode(3);
        input.next.next.next = new ListNode(4);
        input.next.next.next.next = new ListNode(5);
//        input.next.next.next.next.next = new ListNode(5);
        System.out.print(new LinkedListCycle().hasCycle(input));
    }
}
