package top.interview.DynamicProgramming;


public class MaximumSubarray {
    public MaximumSubarray(){

    }

    /**
     * 前面的最大和+当前数  小于 当前数，max = 当前数
     * @param nums
     * @return
     */
    public int maxSubArray_dp(int[] nums) {
        if (nums.length == 0){
            return 0;
        }else if (nums.length == 1){
            return nums[0];
        }
        int length = nums.length;
        int[] dp = new int[length];
        dp[0] = nums[0];
        int max = dp[0];
        for (int i = 1; i < length; i++){
            dp[i] = Math.max(nums[i], dp[i-1] + nums[i]);
            if(max < dp[i]){
                max = dp[i];
            }
        }
        return max;
    }

    public int maxSubArray(int[] nums) {
        if(nums==null || nums.length==0) return 0;
        int sumSoFar = 0;
        int max = Integer.MIN_VALUE;
        for(int num:nums){
            sumSoFar+=num;
            if(num>sumSoFar){
                sumSoFar = num;
            }
            max = Math.max(max,sumSoFar);
        }
        return max;
    }

    public static void main(String[] args) {
        int[] input = new int[]{-2,-1};
        System.out.println(new MaximumSubarray().maxSubArray_dp(input));
    }
}
