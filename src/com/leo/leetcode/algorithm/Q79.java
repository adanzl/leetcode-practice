package com.leo.leetcode.algorithm;

public class Q79 {

    public static void main(String[] args) {
        new Q79().TestOJ();
    }

    public void TestOJ() {
        char[][] board = new char[][]{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
        System.out.println(exist(board, "ABCCED")); // t
        System.out.println(exist(board, "SEE")); // t
        System.out.println(exist(board, "ABCB")); // f
    }

    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (fit(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    boolean fit(char[][] board, int x, int y, String word, int index) {
        if (x < 0 || y < 0 || x > board.length - 1 || y > board[x].length - 1 || board[x][y] != word.charAt(index)) {
            return false;
        }
        if (index == word.length() - 1) return true;

        char c = board[x][y];
        board[x][y] = '.';
        if (fit(board, x - 1, y, word, index + 1)) { // u
            board[x][y] = c;
            return true;
        }
        if (fit(board, x, y - 1, word, index + 1)) { // l
            board[x][y] = c;
            return true;
        }
        if (fit(board, x + 1, y, word, index + 1)) { // d
            board[x][y] = c;
            return true;
        }
        if (fit(board, x, y + 1, word, index + 1)) { // r
            board[x][y] = c;
            return true;
        }
        board[x][y] = c;
        return false;
    }
}
