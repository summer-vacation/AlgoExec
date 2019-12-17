package top.interview;

import java.util.HashSet;

public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        if (isValidCol(board) && isValidRow(board) && isValidPart(board)){
            return true;
        }
        return false;
    }

    public boolean isValidRow(char[][] board){
        int i = 0, j = 0;
        for (j = 0; j < 9; j++) {
            HashSet r = new HashSet();
            for (i = 0; i < 9; i++) {
                char temp = board[j][i];
                if (temp != '.') {
                    if (!r.contains(temp)) {
                        r.add(temp);
                    } else {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public boolean isValidCol(char[][] board){
        int i = 0, j = 0;
        for (j = 0; j < 9; j++) {
            HashSet r = new HashSet();
            for (i = 0; i < 9; i++) {
                char temp = board[i][j];
                if (temp != '.') {
                    if (!r.contains(temp)) {
                        r.add(temp);
                    } else {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public boolean isValidPart(char[][] board){
        int i = 0, j = 0, k = 0, l = 0;
        for (j = 0; j < 9; j = j + 3) {
            for (i = 0; i < 9; i = i + 3) {
                HashSet r = new HashSet();
                for(k=j;k<j+3;k++){
                    for(l=i;l<i+3;l++){
                        char temp = board[k][l];
                        if (temp != '.') {
                            if (!r.contains(temp)) {
                                r.add(temp);
                            } else {
                                return false;
                            }
                        }
                    }
                }
            }
        }
    return true;
    }

    public static void main(String[] args) {
        char[][] input = {
  {'5','3','.','.','7','.','.','.','.'},
  {'6','.','.','1','9','5','.','.','.'},
  {'.','9','8','.','.','.','.','6','.'},
  {'8','.','.','.','6','.','.','.','3'},
  {'4','.','.','8','.','3','.','.','1'},
  {'7','.','.','.','2','.','.','.','6'},
  {'.','6','.','.','.','.','2','8','.'},
  {'.','.','.','4','1','9','.','.','5'},
  {'.','.','.','.','8','.','.','7','9'}
};
        System.out.println(new ValidSudoku().isValidSudoku(input));
    }
}
