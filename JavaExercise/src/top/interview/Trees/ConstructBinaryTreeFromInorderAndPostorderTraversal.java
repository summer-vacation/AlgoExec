package top.interview.Trees;

import java.util.HashMap;

public class ConstructBinaryTreeFromInorderAndPostorderTraversal {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<inorder.length;i++){
            map.put(inorder[i],i);
        }
        return help(inorder,0, inorder.length, postorder,0, postorder.length, map);
    }

    public TreeNode help(int[] in, int left_in, int right_in, int[] post, int left_p, int right_p, HashMap<Integer,Integer> map){
        if(left_p == right_p) return null;

        int root_val = post[right_p-1];
        TreeNode root = new TreeNode(root_val);
        int in_root_index = map.get(root_val);
        int right_num = right_in - in_root_index-1;

        root.left = help(in, left_in, in_root_index, post, left_p,right_p-right_num-1, map);
        root.right = help(in,in_root_index+1, right_in, post,right_p-right_num-1,right_p-1,map);

        return root;
    }

    public static void main(String[] args) {
        int[] in = {9, 3, 15, 20, 7};
        int[] post = {9, 15, 7, 20, 3};
        new ConstructBinaryTreeFromInorderAndPostorderTraversal().buildTree(in, post);
    }
}
