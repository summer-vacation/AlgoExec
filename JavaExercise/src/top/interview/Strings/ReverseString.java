package top.interview.Strings;

public class ReverseString {
    /**
     * https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
     * @param s
     */
    public void reverseString(char[] s) {
        if ((s.length == 0) || (s == null)){
            return;
        }
        int i = 0;
        for(; i < (s.length-1)/2 + 1; i++){
            char temp = s[i];
            s[i] = s[s.length - 1 - i];
            s[s.length - 1 - i] = temp;
        }
        System.out.println(s);
    }

    public static void main(String[] args) {
        ReverseString r = new ReverseString();
        char[] s = null;
        s = new char[]{'h', 'e', 'l', 'l', 'o'};
        r.reverseString(s);
    }
}
