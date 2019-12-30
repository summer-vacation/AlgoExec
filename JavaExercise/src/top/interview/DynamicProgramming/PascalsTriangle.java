package top.interview.DynamicProgramming;

import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/601/
 */
public class PascalsTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        if (numRows == 0){
            return res;
        }
        ArrayList<Integer> row_0 = new ArrayList<>();
        row_0.add(1);
        ArrayList<Integer> row_1 = new ArrayList<>();
        row_1.add(1);
        row_1.add(1);
        if (numRows == 1){
            res.add(row_0);
            return res;
        }
        if (numRows == 2){
            res.add(row_0);
            res.add(row_1);
            return res;
        }
        res.add(row_0);
        res.add(row_1);
        for (int i = 2; i < numRows; i++){
            ArrayList<Integer> row = new ArrayList<>();
            row.add(1);
            for (int j = 1; j < i; j++){
                List<Integer> last_row = res.get(i-1);
                row.add(last_row.get(j) + last_row.get(j-1));
            }
            row.add(1);
            res.add(row);
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.print(new PascalsTriangle().generate(5));
    }
}
