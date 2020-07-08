package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

/**
 * 编写一个程序，通过已填充的空格来解决数独问题。
 * 一个数独的解法需遵循如下规则：
 * 数字 1-9 在每一行只能出现一次。
 * 数字 1-9 在每一列只能出现一次。
 * 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
 * 空白格用 '.' 表示。
 * Note:
 * 给定的数独序列只包含数字 1-9 和字符 '.' 。
 * 你可以假设给定的数独只有唯一解。
 * 给定数独永远是 9x9 形式的。
 * 链接：https://leetcode-cn.com/problems/sudoku-solver
 */
public class Q37 {
    public static void main(String[] args) {
        char[][] board;
        board = LCUtil.stringToChar2dArray("[[\"5\",\"3\",\".\",\".\",\"7\",\".\",\".\",\".\",\".\"],[\"6\",\".\",\".\",\"1\",\"9\",\"5\",\".\",\".\",\".\"],[\".\",\"9\",\"8\",\".\",\".\",\".\",\".\",\"6\",\".\"],[\"8\",\".\",\".\",\".\",\"6\",\".\",\".\",\".\",\"3\"],[\"4\",\".\",\".\",\"8\",\".\",\"3\",\".\",\".\",\"1\"],[\"7\",\".\",\".\",\".\",\"2\",\".\",\".\",\".\",\"6\"],[\".\",\"6\",\".\",\".\",\".\",\".\",\"2\",\"8\",\".\"],[\".\",\".\",\".\",\"4\",\"1\",\"9\",\".\",\".\",\"5\"],[\".\",\".\",\".\",\".\",\"8\",\".\",\".\",\"7\",\"9\"]]");
        new Q37().solveSudoku(board);
        System.out.println(LCUtil.char2dToString(board));
    }

    public void solveSudoku(char[][] board) {
        boolean[][] col = new boolean[9][9], row = new boolean[9][9], box = new boolean[9][9];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                int v = board[i][j] - '1';
                col[j][v] = true;
                row[i][v] = true;
                box[j / 3 * 3 + i / 3][v] = true;
            }
        }
        dfs(board, col, row, box, 0, 0);
    }

    boolean dfs(char[][] board, boolean[][] col, boolean[][] row, boolean[][] box, int i, int j) {
        while (board[i][j] != '.') {
            if (++j >= 9) {
                i++;
                j = 0;
            }
            if (i >= 9) return true;
        }
        int k = j / 3 * 3 + i / 3;
        for (int v = 0; v < 9; v++) {
            if (!col[j][v] && !row[i][v] && !box[k][v]) {
                col[j][v] = true;
                row[i][v] = true;
                box[k][v] = true;
                board[i][j] = (char) (v + '1');
                if (dfs(board, col, row, box, i, j))
                    return true;
                col[j][v] = false;
                row[i][v] = false;
                box[k][v] = false;
                board[i][j] = '.';
            }
        }
        return false;
    }

}
