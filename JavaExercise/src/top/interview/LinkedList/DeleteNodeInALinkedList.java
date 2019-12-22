package top.interview.LinkedList;

public class DeleteNodeInALinkedList {
    /**
     * https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
     * @param node
     */
    public void deleteNode(ListNode node) {
        if (node.next != null){
            if (node.next.next != null){
                node.val = node.next.val;
                node.next = node.next.next;
            }else {
                node.val = node.next.val;
                node.next = null;
            }
        }
    }

    public static void main(String[] args) {
        ListNode root = new ListNode(4);
        root.next = new ListNode(5);
        root.next.next = new ListNode((1));
        root.next.next.next = new ListNode(9);
        new DeleteNodeInALinkedList().deleteNode(root);
    }
}
