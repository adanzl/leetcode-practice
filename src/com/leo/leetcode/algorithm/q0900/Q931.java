package com.leo.leetcode.algorithm.q0900;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
 * 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
 * 在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
 * 具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
 * 提示：
 * 1、n == matrix.length == matrix[i].length
 * 2、1 <= n <= 100
 * 3、-100 <= matrix[i][j] <= 100
 * 链接：https://leetcode-cn.com/problems/minimum-falling-path-sum
 */
public class Q931 {

    public static void main(String[] args) {
        // -48
        System.out.println(new Q931().minFallingPathSum(stringToInt2dArray("[[-48]]")));
        // 13
        System.out.println(new Q931().minFallingPathSum(stringToInt2dArray("[[2,1,3],[6,5,4],[7,8,9]]")));
        // -59
        System.out.println(new Q931().minFallingPathSum(stringToInt2dArray("[[-19,57],[-40,-5]]")));
    }

    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length, ret = Integer.MAX_VALUE;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int v = matrix[i - 1][j];
                if (j > 0) v = Math.min(v, matrix[i - 1][j - 1]);
                if (j < n - 1) v = Math.min(v, matrix[i - 1][j + 1]);
                matrix[i][j] += v;
            }
        }
        for (int i = 0; i < n; i++) ret = Math.min(ret, matrix[n - 1][i]);
        return ret;
    }
}
