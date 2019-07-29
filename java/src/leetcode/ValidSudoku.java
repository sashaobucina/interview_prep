package leetcode;

import java.util.HashSet;
import java.util.Set;

public class ValidSudoku {

  private boolean notInRow(char[][] board, int row) {
    Set<Character> set = new HashSet<>();
    for (int i = 0; i < 9; i++) {
      char curr = board[row][i];
      if (set.contains(curr))
        return false;
      if (curr != '.')
        set.add(curr);
    }
    return true;
  }

  private boolean notInCol(char[][] board, int col) {
    Set<Character> set = new HashSet<>();
    for (int i = 0; i < 9; i++) {
      char curr = board[i][col];
      if (set.contains(curr))
        return false;
      if (curr != '.')
        set.add(curr);
    }
    return true;
  }

  private boolean notInBox(char[][] board, int row, int col) {
    Set<Character> set = new HashSet<>();
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        char curr = board[i][j];
        if (set.contains(curr))
          return false;
        if (curr != '.')
          set.add(curr);
      }
    }
    return true;
  }

  private boolean isValid(char[][] board, int row, int col) {
    return this.notInRow(board, row) && this.notInCol(board, col) &&
      this.notInBox(board, row - row % 3, col - col % 3);
  }

  public boolean isValidSudoku(char[][] board) {
    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        if (!this.isValid(board, i, j)) {
          return false;
        }
      }
    }
    return true;
  }

  public static void main(String[] args) {
    char[][] board = {
      {'8','3','.','.','7','.','.','.','.'},
      {'6','.','.','1','9','5','.','.','.'},
      {'.','9','8','.','.','.','.','6','.'},
      {'8','.','.','.','6','.','.','.','3'},
      {'4','.','.','8','.','3','.','.','1'},
      {'7','.','.','.','2','.','.','.','6'},
      {'.','6','.','.','.','.','2','8','.'},
      {'.','.','.','4','1','9','.','.','5'},
      {'.','.','.','.','8','.','.','7','9'}
    };
    ValidSudoku validator = new ValidSudoku();
    System.out.println(validator.isValidSudoku(board));
  }
}