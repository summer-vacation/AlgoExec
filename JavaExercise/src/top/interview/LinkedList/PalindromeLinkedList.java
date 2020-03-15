package top.interview.LinkedList;


/***
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/772/
 * 判断回文链
 * O(n) time and O(1) space
 * 使用异或不行！！！！！ 1、3、0、2异或结果为0…
 *
 */
public class PalindromeLinkedList {
    public boolean isPalindrome(ListNode head) {
        // 如果为null链表或者链表长度为1，则一定是false
        if (head == null || head.next == null){
            return true;
        }
        int res = head.val;
        ListNode fast = head;
        ListNode slow = head;
        int length = 1;

        return false;
    }

    public static void main(String[] args) {
        ListNode input = new ListNode(1);
        input.next = new ListNode(3);
        input.next.next = new ListNode(0);
        input.next.next.next = new ListNode(2);
//        input.next.next.next.next = new ListNode(1);
        System.out.print(new PalindromeLinkedList().isPalindrome(input));
    }
}
