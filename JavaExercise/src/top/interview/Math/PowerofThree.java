package top.interview.Math;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/745/
 * 求log3为底数的对数结果，
 * Math中没有直接3为底数的，所以，使用换底公式
 * 存在的问题： 利用换底公式计算出来的可能是一个极限接近某一个整数的小数
 * 可用的底 e、10
 * 比如：243、177148
 */
public class PowerofThree {
    public boolean isPowerOfThree(int n) {
        if (n == 0){
            return false;
        }
        double res = Math.log10(n)/Math.log10(3);
        System.out.println(res % 1);
        if (res % 1 == 0) return true;
        else return false;
    }

    public static void main(String[] args) {
        int input = 177148;
        System.out.println(new PowerofThree().isPowerOfThree(input));
    }
}
