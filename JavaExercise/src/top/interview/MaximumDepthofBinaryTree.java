package top.interview;

public class MaximumDepthofBinaryTree {
    public MaximumDepthofBinaryTree(){
    }

    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        if (root.left == null && root.right == null){
            return 1;
        } else {
            return Math.max(1 + maxDepth(root.left), 1+ maxDepth(root.right));
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(9);
        root.right.right.right = new TreeNode(11);

        System.out.println(new MaximumDepthofBinaryTree().maxDepth(root));
    }
}

class TreeNode {
 int val;
 TreeNode left;
 TreeNode right;
 TreeNode(int x) { val = x; }
 }