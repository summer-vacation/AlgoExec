package top.interview.Trees;

import java.util.ArrayDeque;

/**
 * https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
 */
public class MaximumDepthofBinaryTree {
    public MaximumDepthofBinaryTree(){
    }

    /**
     * 递归
     * @param root
     * @return
     */
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        int left = 1 + maxDepth(root.left);
        int right = 1+ maxDepth(root.right);
        return Math.max(left, right);
//        if (root.left == null && root.right == null){
//            return 1;
//        } else {
//            return Math.max(1 + maxDepth(root.left), 1+ maxDepth(root.right));
//        }
    }

    /***
     * 广度优先遍历,非递归
     * @param root
     * @return 深度
     */
    public int maxDepth_2(TreeNode root){
        if (root == null){
            return 0;
        }
        ArrayDeque<TreeNode> queue=new ArrayDeque<TreeNode>();
        // LinkedList<TreeNode> linkedList = new LinkedList<>();
        int height=0;
        queue.add(root);
        while(!queue.isEmpty()){
            int size=queue.size();
            for(int i=0;i<size;i++){
                TreeNode node=queue.remove();
                if(null!=node.left){
                    queue.add(node.left);
                }
                if(null!=node.right){
                    queue.add(node.right);
                }
            }
            height++;
        }
        return height;
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