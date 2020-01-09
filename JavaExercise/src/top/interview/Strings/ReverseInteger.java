package top.interview.Strings;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/880/
 * 注意 负号、0的位置
 * int的范围： [−2^31,  2^31 − 1]，不在范围内时的输出
 *
 * todo：优化下？
 */
public class ReverseInteger {
    public int reverse(int x) {
        if (x == 0){
            return 0;
        }
        String s = Integer.toString(x);
//        System.out.println(s);
        StringBuilder sb = new StringBuilder();
        if (s.charAt(0) == '-'){
            sb.append('-');
            s = s.substring(1, s.length());
        }
//        System.out.println(s);
        for (int i = s.length()-1; i >= 0; i--){
            char temp = s.charAt(i);
            if ((sb.length() == 1 && sb.charAt(0)=='-') && temp == '0') continue;
            sb.append(temp);
        }
        if (Double.parseDouble(sb.toString()) > Integer.MAX_VALUE
        || Double.parseDouble(sb.toString()) < Integer.MIN_VALUE){
            return 0;
        }
        return Integer.parseInt(sb.toString());
    }

    public static void main(String[] args) {
        System.out.println(new ReverseInteger().reverse(102));
    }
}
