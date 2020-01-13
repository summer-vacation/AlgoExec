package top.interview.other;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/565/
 * java有接口。
 */
public class Numberof1Bits {

    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        return Integer.bitCount(n);
//        java接口源码
//        i = i - ((i >>> 1) & 0x55555555);
//        i = (i & 0x33333333) + ((i >>> 2) & 0x33333333);
//        i = (i + (i >>> 4)) & 0x0f0f0f0f;
//        i = i + (i >>> 8);
//        i = i + (i >>> 16);
//        return i & 0x3f;
    }

    public static void main(String[] args) {
        System.out.println(new Numberof1Bits().hammingWeight(-3));
    }
}
