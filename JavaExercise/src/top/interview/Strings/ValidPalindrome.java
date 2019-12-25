package top.interview.Strings;


public class ValidPalindrome {
    /**
     * 考虑非字母、大小写、空格等情况
     * https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/883/
     * @param s
     * @return
     */
    public boolean isPalindrome(String s) {
        char[] array = s.toLowerCase().toCharArray();
        StringBuilder sb = new StringBuilder();
        for (char c : array){
            if (Character.isLetterOrDigit(c)){
                sb.append(c);
            }
        }
//        System.out.println(sb.toString());
//        System.out.println(sb.reverse().toString());
        // 先sb.toString(); 再sb.reverse().toString()
        return sb.toString().equals(sb.reverse().toString());
    }

    public static void main(String[] args) {
        String input = "race a car";
        System.out.println(new ValidPalindrome().isPalindrome(input));
    }
}
