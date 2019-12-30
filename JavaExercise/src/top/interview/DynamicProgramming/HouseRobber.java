package top.interview.DynamicProgramming;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/576/
 * 不能连续取
 * 动态规划，，要想清楚推导式！！
 * dp[i] = Math.max(dp[i-2], dp[i-3]) + nums[i-1];
 */
public class HouseRobber {
    public int rob(int[] nums) {
        if (nums.length == 0 || nums == null){
            return 0;
        } else if (nums.length == 1){
            return nums[0];
        }
        int[] dp = new int[nums.length+1];
        dp[0] = 0;
        dp[1] = nums[0];
        dp[2] = nums[1];
        for (int i= 3; i <= nums.length; i = i+1){
            dp[i] = Math.max(dp[i-2], dp[i-3]) + nums[i-1];
        }
        return Math.max(dp[nums.length], dp[nums.length-1]);
    }

    public static void main(String[] args) {
        int[] input = {2,1,1,2};
        System.out.print(new HouseRobber().rob(input));
    }
}
