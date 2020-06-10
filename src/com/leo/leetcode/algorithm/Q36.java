package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q36 {

    public static void main(String[] args) {
        new Q36().TestOJ();
    }

    public void TestOJ() {
        System.out.println(isValidSudoku(LCUtil.stringToChar2dArray("[[\"5\",\"3\",\"6\",\".\",\"7\",\".\",\".\",\".\",\".\"],[\"6\",\".\",\".\",\"1\",\"9\",\"5\",\".\",\".\",\".\"],[\".\",\"9\",\"8\",\".\",\".\",\".\",\".\",\"6\",\".\"],[\"8\",\".\",\".\",\".\",\"6\",\".\",\".\",\".\",\"3\"],[\"4\",\".\",\".\",\"8\",\".\",\"3\",\".\",\".\",\"1\"],[\"7\",\".\",\".\",\".\",\"2\",\".\",\".\",\".\",\"6\"],[\".\",\"6\",\".\",\".\",\".\",\".\",\"2\",\"8\",\".\"],[\".\",\".\",\".\",\"4\",\"1\",\"9\",\".\",\".\",\"5\"],[\".\",\".\",\".\",\".\",\"8\",\".\",\".\",\"7\",\"9\"]]")));
    }

    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            if (check(board, 8, 0, i, i)) return false;
        }
        for (int i = 0; i < board[0].length; i++) {
            if (check(board, i, i, 8, 0)) return false;
        }
        for (int i = 0; i < 9; i++) {
            int w = i / 3 * 3;
            int h = i % 3 * 3;
            if (check(board, w + 2, w, h + 2, h)) return false;
        }
        return true;
    }

    private boolean check(char[][] board, int maxW, int minW, int maxH, int minH) {
        int[] arr = new int[9];
        for (int i = minW; i <= maxW; i++) {
            for (int j = minH; j <= maxH; j++) {
                int v = board[i][j];
                if (v == '.') continue;
                v -= '1';
                if (arr[v] == 1) {
                    return true;
                }
                arr[v] = 1;
            }
        }

        return false;
    }
}
