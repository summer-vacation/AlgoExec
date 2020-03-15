package top.interview.Trees;

public class ConvertSortedArraytoBinarySearchTree {
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length == 0)
            return null;
        else
            return createBST(nums,0,nums.length-1);

    }

    public TreeNode createBST(int[] n, int s, int e)
    {
        if(s>e)
            return null;
        int mid=(s+e)/2;
        TreeNode temp= new TreeNode(n[mid]);
        temp.left= createBST(n,s,mid-1);
        temp.right=createBST(n,mid+1,e);
        return temp;
    }

    public static void main(String[] args) {
        int[] input = {-10, -3, 0, 5, 9};
        new ConvertSortedArraytoBinarySearchTree().sortedArrayToBST(input);
    }
}
