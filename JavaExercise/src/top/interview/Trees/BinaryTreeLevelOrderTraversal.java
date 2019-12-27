package top.interview.Trees;

import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.List;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/628/
 * 每一层存一个list
 */
public class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> treeLevel = new LinkedList<>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root ==  null){
            return treeLevel;
        }
        ArrayDeque<TreeNode> queue=new ArrayDeque<TreeNode>();
        queue.add(root);
        LinkedList<Integer> root_level = new LinkedList<>();
        root_level.add(root.val);
        treeLevel.add(root_level);
        while(!queue.isEmpty()){
            int size=queue.size();
            LinkedList<Integer> level = new LinkedList<>();
            for(int i=0;i<size;i++){
                TreeNode node=queue.removeFirst();
                if(null!=node.left){
                    queue.add(node.left);
                    level.add(node.left.val);
                }
                if(null!=node.right){
                    queue.add(node.right);
                    level.add(node.right.val);
                }
            }
            if (level.size() != 0) {
                treeLevel.add(level);
            }
        }
        return treeLevel;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(1);
        root.right = new TreeNode(4);
        root.left.left = new TreeNode(3);
        root.right.right = new TreeNode(6);
//        root.left.left = new TreeNode(3);
//        root.left.right = new TreeNode(6);
        System.out.println(new BinaryTreeLevelOrderTraversal().levelOrder(root));
    }
}
