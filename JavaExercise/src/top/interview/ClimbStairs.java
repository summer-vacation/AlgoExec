package top.interview;

/***
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/569/
 *
 * 画图理解、、、列方程
 */
public class ClimbStairs {
    public ClimbStairs(){

    }
    public int climbStairs(int n) {
        if (n == 0 || n == 1 || n == 2) {
            return n;
        }else {
            int[] steps = new int[n];
            steps[0] = 1;
            steps[1] = 2;
            for (int i = 2; i < n; i++){
                steps[i] = steps[i-1] + steps[i-2];
            }
            return steps[n-1];
        }
    }

    public static void main(String[] args) {
        System.out.println(new ClimbStairs().climbStairs(3));
    }
}
