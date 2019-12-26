package top.interview.Strings;

import java.util.ArrayList;

public class ImplementstrStr {
    /**
     * https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/885/
     * 实现String的indexOf
     * @param haystack
     * @param needle
     * @return
     */
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0 || needle == null){
            return 0;
        }
        char[] array = haystack.toCharArray();
        char[] array_needle = needle.toCharArray();
        int i = 0, j = 0;
        for (i = 0; i < haystack.length() - needle.length()+1; i++){
            for (j = 0; j < needle.length(); j++){
                if (array[i+j] != array_needle[j]){
                   break;
                }
            }
            if (j == needle.length()) return i;
        }

        return -1;
    }

    public static void main(String[] args) {
        String haystack = "heello", needle = "ll";
        System.out.println(new ImplementstrStr().strStr(haystack, needle));
    }
}
