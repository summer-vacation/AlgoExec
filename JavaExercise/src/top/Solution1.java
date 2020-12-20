package top;

public class Solution1 {
    public static boolean isLowercaseLetter(char c) {
        return c >= 'a' && c <= 'z';
    }

    public static String solution(String x) {
        String ret = "";
        for(int i=0;i < x.length();i++){
            char c = x.charAt(i);
            if (isLowercaseLetter(c)) {
                ret += (char)('a' + 'z' - c);
            }
            else {
                ret += c;
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        System.out.println(Solution1.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!   "));
    }
}