package top.interview.other;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/648/
 * java 有接口。还有一个类似的接口 reverseBytes
 * reverse是按位反转
 * reverseBytes是按byte反转
 */
public class ReverseBits {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        return Integer.reverse(n);
//        源码：
//        i = (i & 0x55555555) << 1 | (i >>> 1) & 0x55555555;
//        i = (i & 0x33333333) << 2 | (i >>> 2) & 0x33333333;
//        i = (i & 0x0f0f0f0f) << 4 | (i >>> 4) & 0x0f0f0f0f;
//        i = (i << 24) | ((i & 0xff00) << 8) |
//            ((i >>> 8) & 0xff00) | (i >>> 24);
//        return i;
    }

    public static void main(String[] args) {
        System.out.println(new ReverseBits().reverseBits(43261596));
    }
}
