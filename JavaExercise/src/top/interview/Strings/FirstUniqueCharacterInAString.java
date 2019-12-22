package top.interview.Strings;

public class FirstUniqueCharacterInAString {
    public int firstUniqChar(String s) {
        if (s.length() == 0 || s == null){
            return -1;
        }
        int[] nums = new int[26];
        char[]  sArray = s.toCharArray();
        for (int i = 0; i < s.length(); i++){
            nums[(int)sArray[i]-'a']++;
        }
        for (int i = 0; i < s.length(); i++){
            if (nums[s.charAt(i)-'a'] == 1){
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String inpput = "leetcode";
        System.out.println(new FirstUniqueCharacterInAString().firstUniqChar(inpput));
    }
}
