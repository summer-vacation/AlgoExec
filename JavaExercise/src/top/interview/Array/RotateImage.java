package top.interview.Array;

public class RotateImage {
    /**
     * https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
     * @param matrix
     */
    public void rotate(int[][] matrix) {
        int num = matrix.length;
        if(num <= 1){
            return;
        }
        int i, j;
        for (i=0; i < (num-1)/2+1; i++){
            int[] temp = matrix[i];
            matrix[i] = matrix[num -1 -i];
            matrix[num -1 -i] = temp;
        }

        for (i=0; i < num; i++) {
            for (j = i+1; j < num; j++){
               int tep = matrix[i][j];
               matrix[i][j] = matrix[j][i];
               matrix[j][i] = tep;
            }
        }
        return;
    }
}
