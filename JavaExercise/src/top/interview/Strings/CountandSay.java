package top.interview.Strings;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/886/
 * 连续相同的数字要合并
 */
public class CountandSay {
    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        String res = countAndSay(n - 1);
        StringBuilder sb = new StringBuilder();
        int i = 0, countSame = 0;
        for (i = 0; i <= res.length(); i++) {
            if (i == res.length() || (i > 0 && res.charAt(i) != res.charAt(i - 1))) {
                sb.append(countSame);
                sb.append(res.charAt(i - 1));
                countSame = 0;
            }
            countSame++;
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        int input = 10;
        System.out.println(new CountandSay().countAndSay(input));
    }
}
