package com.leo.leetcode.algorithm.q1300;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.int2dArrayToString;

/**
 * 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和：
 * 1、i - k <= r <= i + k,
 * 2、j - k <= c <= j + k 且
 * 3、(r, c) 在矩阵内。
 * 提示：
 * 1、m == mat.length
 * 2、n == mat[i].length
 * 3、1 <= m, n, k <= 100
 * 4、1 <= mat[i][j] <= 100
 * 链接：https://leetcode-cn.com/problems/matrix-block-sum
 */
public class Q1314 {

    public static void main(String[] args) {
        // [[12,21,16],[27,45,33],[24,39,28]]
        System.out.println(int2dArrayToString(new Q1314().matrixBlockSum(stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]"), 1)));
        // [[45,45,45],[45,45,45],[45,45,45]]
        System.out.println(int2dArrayToString(new Q1314().matrixBlockSum(stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]"), 2)));
    }

    public int[][] matrixBlockSum(int[][] mat, int k) {
        int row = mat.length, col = mat[0].length;
        int[][] ret = new int[row][col], flags = new int[row][col];
        flags[0][0] = mat[0][0];
        for (int i = 1; i < row; i++) flags[i][0] = flags[i - 1][0] + mat[i][0];
        for (int i = 1; i < col; i++) flags[0][i] = flags[0][i - 1] + mat[0][i];
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                flags[i][j] = mat[i][j] + flags[i - 1][j] + flags[i][j - 1] - flags[i - 1][j - 1];
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int min_x = i - k - 1, min_y = j - k - 1;
                int max_x = Math.min(i + k, row - 1), max_y = Math.min(j + k, col - 1);
                ret[i][j] = flags[max_x][max_y];
                if (min_x >= 0 && min_y >= 0) {
                    ret[i][j] += flags[min_x][min_y];
                    ret[i][j] -= flags[min_x][max_y];
                    ret[i][j] -= flags[max_x][min_y];
                } else if (min_x >= 0) {
                    ret[i][j] -= flags[min_x][max_y];
                } else if (min_y >= 0) {
                    ret[i][j] -= flags[max_x][min_y];
                }
            }
        }
        return ret;
    }
}
