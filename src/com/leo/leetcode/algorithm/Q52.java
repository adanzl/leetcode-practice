package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 * 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
 * 链接：https://leetcode-cn.com/problems/n-queens-ii
 */
public class Q52 {
    public static void main(String[] args) {
        System.out.println(new Q52().totalNQueens(0)); // 0
        System.out.println(new Q52().totalNQueens(4)); // 2
    }

    public int totalNQueens(int n) {
        char[][] matrix = new char[n][];
        for (int i = 0; i < n; i++) {
            matrix[i] = new char[n];
            Arrays.fill(matrix[i], '.');
        }
        return solve(matrix, n, 0, 0, new int[n], new int[n]);
    }

    int solve(char[][] matrix, int piece, int offsetI, int offsetJ, int[] row, int[] col) {
        if (piece == 0) return 1;
        int out = 0;
        for (int i = offsetI; i < matrix.length; i++) {
            if (row[i] == 1) continue;
            for (int j = i == offsetI ? offsetJ : 0; j < matrix[i].length; j++) {
                if (col[j] == 1) continue;
                if (unConflict(matrix, i, j)) {
                    row[i] = 1;
                    col[j] = 1;
                    matrix[i][j] = 'Q';
                    out += solve(matrix, piece - 1, i, j, row, col);
                    row[i] = 0;
                    col[j] = 0;
                    matrix[i][j] = '.';
                }
            }
        }
        return out;
    }

    boolean unConflict(char[][] matrix, int i, int j) {
        int n = matrix.length;
        for (int k = 0; i + k < n && j - k >= 0; k++) if (matrix[i + k][j - k] == 'Q') return false;
        for (int k = 0; i - k >= 0 && j + k < n; k++) if (matrix[i - k][j + k] == 'Q') return false;
        for (int k = 0; i + k < n && j + k < n; k++) if (matrix[i + k][j + k] == 'Q') return false;
        for (int k = 0; i - k >= 0 && j - k >= 0; k++) if (matrix[i - k][j - k] == 'Q') return false;
        return true;
    }
}
