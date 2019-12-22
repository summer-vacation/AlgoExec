package top.interview.Strings;

public class ValidAnagram {
    /**
     * https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
     * @param s
     * @param t
     * @return
     */
    public boolean isAnagram(String s, String t) {
        if (s.length() ==0 && t.length() == 0){
            return true;
        }else if(s.length() != t.length()) {
            return false;
        } else {
            StringBuilder sb = new StringBuilder(s);
            for (int i = 0; i < t.length(); i++) {
                int index = s.indexOf(t.charAt(i));
                if (index == -1) {
                    return false;
                } else{
                    s = sb.deleteCharAt(index).toString();
                    // System.out.println(s);
                }
            }
            return true;
        }
    }

    public static void main(String[] args) {
        String s = "ccac", t = "aacc";
        System.out.println(new ValidAnagram().isAnagram(s, t));
    }
}
