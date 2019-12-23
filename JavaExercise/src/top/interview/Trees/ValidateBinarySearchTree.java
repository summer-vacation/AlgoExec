package top.interview.Trees;

import java.util.ArrayList;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/625/
 */
public class ValidateBinarySearchTree {
    ArrayList<Integer> elements = new ArrayList<>();

    public boolean isValidBST(TreeNode root) {
        return helper(root);
    }

    public boolean helper(TreeNode root){
        if (root==null) return true;
        boolean left = helper(root.left);
        if (elements.size() != 0 && root.val <= elements.get(elements.size()-1)) return false;
        elements.add(root.val);
        boolean right = helper(root.right);
        return left && right;
    }
    /**
     * 1、先按需放入ArrayList
     * 2、循环比较大小
     * @param root
     * @return
     */
    public boolean isValidBST1(TreeNode root) {
        if (root == null){
            return true;
        }
        inorder(root);
        for(int i = 0;i<elements.size()-1;i++)
        {
            if(elements.get(i) >= elements.get(i+1))
                return false;
        }
        return true;
    }

    public void inorder(TreeNode root)
    {
        if(root == null)
            return;

        inorder(root.left);
        elements.add(root.val);
        inorder(root.right);

    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(1);
        root.right = new TreeNode(4);
        root.right.left = new TreeNode(3);
        root.right.right = new TreeNode(6);

        System.out.println(new ValidateBinarySearchTree().isValidBST(root));
    }
}
