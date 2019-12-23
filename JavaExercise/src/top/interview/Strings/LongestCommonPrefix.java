package top.interview.Strings;

public class LongestCommonPrefix {

    /**
     * https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
     * @param strs
     * @return
     */
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0){
            return "";
        }
        int i = 0, j = 0;
        StringBuilder prefix = new StringBuilder();
        for (i = 0; i < strs[0].length(); i++){
            char a = strs[0].charAt(i);
            for (j = 1; j < strs.length; j ++){
                if (i < strs[j].length()){
                    if (strs[j].charAt(i) != a){
                        break;
                    }
                }else{
                    break;
                }
            }
            if (j == strs.length) {
                prefix = prefix.append(a);
            }else {
                break;
            }
        }
        return prefix.toString();
    }

    public static void main(String[] args) {
        String[] input = {"aa","a"};
        System.out.println(new LongestCommonPrefix().longestCommonPrefix(input));
    }
}
