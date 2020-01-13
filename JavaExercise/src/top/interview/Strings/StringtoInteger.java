package top.interview.Strings;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/884/
 * 1、去掉首位空格
 * 2、判断是否带正负号、是否是数字、字母
 */
public class StringtoInteger {
    public int myAtoi(String str) {
        str = str.trim();
        StringBuilder sb = new StringBuilder(str);
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < sb.length(); i++){
            if (i == 0 && (sb.charAt(0) == '-' || sb.charAt(0) == '+')){
                res.append(sb.charAt(i));
                continue;
            }
            if (Character.isDigit(sb.charAt(i))){
                res.append(sb.charAt(i));
            }else {
                break;
            }
        }
        double d = 0;
        try {
            d = Double.valueOf(res.toString());
        }catch (Exception e){
            return 0;
        }
        if (d > Integer.MAX_VALUE){
            return Integer.MAX_VALUE;
        }
        if (d < Integer.MIN_VALUE){
            return Integer.MIN_VALUE;
        }
        return (int)d;
    }

    public static void main(String[] args) {
        System.out.println(new StringtoInteger().myAtoi("   +0 123"));
    }
}
