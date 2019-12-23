package top.interview.SortingAndSearching;

public class MergeSortedArray {
    public MergeSortedArray(){

    }

    /***
     * https://leetcode.com/explore/featured/card/top-interview-questions-easy/96/sorting-and-searching/587/
     * 空间换时间
     * @param nums1  有足够用的空间
     * @param m   有效的个数
     * @param nums2
     * @param n
     * @return
     */
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] nums3 = new int[m];
        for (int i = 0; i < m; i++) {
            nums3[i] = nums1[i];
        }
        int l = 0;
        int k = 0;
        int num2 = 0;
        int num3 = 0;
        for (int i = 0; i < nums1.length; i++) {
            if (l >= m){
                num3 = Integer.MAX_VALUE;
            }else{
                num3 = nums3[l];
            }
            if (k >= n){
                num2 = Integer.MAX_VALUE;
            }else{
                num2 = nums2[k];
            }

            if (num3 < num2 && l < m) {
                nums1[i] = num3;
                l++;
            }

            if (num3 >= num2 && k < n){
                nums1[i] = num2;
                k++;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums1 = new int[]{1};
        int m = 1;
        int[] nums2 = new int[]{};
        int n = 0;
        new MergeSortedArray().merge(nums1, m, nums2, n);
    }
}
