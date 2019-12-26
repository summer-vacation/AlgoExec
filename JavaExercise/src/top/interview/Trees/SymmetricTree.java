package top.interview.Trees;

public class SymmetricTree {

    /**
     * https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/627/
     * 检查对称树，Symmetric：对称
     * @param root
     * @return
     */
    public boolean isSymmetric(TreeNode root) {
        if (root == null){
            return true;
        }
        return compareLeftRight(root.left, root.right);
    }

    private boolean compareLeftRight(TreeNode left, TreeNode right){
        if (left == null && right == null) return true;
        if (left == null || right == null) return false;

        return left.val == right.val
                && compareLeftRight(left.left, right.right)
                && compareLeftRight(left.right, right.left);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(9);
        root.left.left = new TreeNode(5);
        root.right.left = new TreeNode(4);

        System.out.println(new SymmetricTree().isSymmetric(root));
    }
}
