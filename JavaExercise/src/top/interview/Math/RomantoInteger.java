package top.interview.Math;

import java.util.LinkedHashMap;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/878/
 *
 */
public class RomantoInteger {
    public int romanToInt(String s) {
        if (s.length() == 0){
            return 0;
        }
        LinkedHashMap<Character, Integer> base = new LinkedHashMap<>();
        base.put('I', 1);
        base.put('V', 5);
        base.put('X', 10);
        base.put('L', 50);
        base.put('C', 100);
        base.put('D', 500);
        base.put('M', 1000);
        int length = s.length();
        int res = 0;
        for (int i = 0; i < length; i++){
            if (i < length-1 && s.charAt(i)=='I' && s.charAt(i+1)=='V'){
                res += 4;
                i++;
                continue;
            }
            if (i < length-1 && s.charAt(i)=='I' && s.charAt(i+1)=='X'){
                res += 9;
                i++;
                continue;
            }
            if (i < length-1 && s.charAt(i)=='X' && s.charAt(i+1)=='L'){
                res += 40;
                i++;
                continue;
            }
            if (i < length-1 && s.charAt(i)=='X' && s.charAt(i+1)=='C'){
                res += 90;
                i++;
                continue;
            }
            if (i < length-1 && s.charAt(i)=='C' && s.charAt(i+1)=='D'){
                res += 400;
                i++;
                continue;
            }
            if (i < length-1 && s.charAt(i)=='C' && s.charAt(i+1)=='M'){
                res += 900;
                i++;
                continue;
            }
            res += base.get(s.charAt(i));
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(new RomantoInteger().romanToInt("IV"));
    }
}
