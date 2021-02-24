package com.leo.leetcode.algorithm.q0800;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.int2dArrayToString;

/**
 * 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
 * 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
 * <p>
 * 提示：
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 1000
 * 1 <= m * n <= 10^5
 * -10^9 <= matrix[i][j] <= 10^9
 * <p>
 * 链接：https://leetcode-cn.com/problems/transpose-matrix
 */
public class Q867 {

    public static void main(String[] args) {
        // [[1,4,7],[2,5,8],[3,6,9]]
        System.out.println(int2dArrayToString(new Q867().transpose(stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]"))));
        // [[1,4],[2,5],[3,6]]
        System.out.println(int2dArrayToString(new Q867().transpose(stringToInt2dArray("[[1,2,3],[4,5,6]]"))));
    }

    public int[][] transpose(int[][] matrix) {
        int r = matrix.length, c = matrix[0].length;
        int[][] ret = new int[c][r];
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                ret[j][i] = matrix[i][j];
        return ret;
    }
}
