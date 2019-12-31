package top.interview.other;

import sun.nio.cs.FastCharsetProvider;

import java.util.Stack;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/721/
 * 括号匹配
 */
public class ValidParentheses {
    public boolean isValid(String s) {
        if(s.length() % 2 != 0){
            return false;
        }
        Stack<Character> temp = new Stack<>();
        for (char c : s.toCharArray()){
            if ('(' == c || '{' == c || '[' == c){
                temp.push(c);
            }
            if (')' == c){
                if (temp.empty() || '(' != temp.pop()){
                    return false;
                }
            }else if ('}' == c){
                if (temp.empty() || '{' != temp.pop()){
                    return false;
                }
            }else if (']' == c){
                if (temp.empty() || '[' != temp.pop()){
                    return false;
                }
            }
        }
        if (temp.empty())
            return true;
        else return false;
    }

    public static void main(String[] args) {
        String input = "){";
        System.out.print(new ValidParentheses().isValid(input));
    }
}
