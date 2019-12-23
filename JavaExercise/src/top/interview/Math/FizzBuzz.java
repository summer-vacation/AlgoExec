package top.interview.Math;

import java.util.LinkedList;
import java.util.List;

public class FizzBuzz {
    public FizzBuzz(){

    }

    /**
     * https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/
     * @param n
     * @return
     */
    public List<String> fizzBuzz(int n) {
        LinkedList<String> res = new LinkedList<>();
        if (n == 0){
            return null;
        }

        for (int i=1; i <= n; i++){
            if (i%15 == 0){
                res.add("FizzBuzz");
            }else if (i%5 == 0){
                res.add("Buzz");
            }else if (i%3 == 0){
                res.add("Fizz");
            }else{
                res.add(Integer.toString(i));
            }
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.print(new FizzBuzz().fizzBuzz(15));
    }
}
