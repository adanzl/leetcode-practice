package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。
 * 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
 * <p>
 * 说明:
 * 1、你可以假设矩阵不可变。
 * 2、会多次调用 sumRegion 方法。
 * 3、你可以假设 row1 ≤ row2 且 col1 ≤ col2。
 * <p>
 * 链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable
 */
public class Q304 {

    public static void main(String[] args) {
        NumMatrix obj;
        obj = new NumMatrix(stringToInt2dArray("[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]"));
        System.out.println(obj.sumRegion(2, 1, 4, 3)); // 8
        System.out.println(obj.sumRegion(1, 1, 2, 2)); // 11
        System.out.println(obj.sumRegion(1, 2, 2, 4)); // 12
    }

    static class NumMatrix {

        int[][] sums;

        public NumMatrix(int[][] matrix) {
            int nRow = matrix.length;
            if (nRow == 0) return;
            int nCol = matrix[0].length;
            sums = new int[nRow + 1][nCol + 1];
            for (int i = 0; i < nRow; i++) {
                for (int j = 0; j < nCol; j++) {
                    sums[i + 1][j + 1] = sums[i + 1][j] + sums[i][j + 1] - sums[i][j] + matrix[i][j];
                }
            }
        }

        public int sumRegion(int row1, int col1, int row2, int col2) {
            return sums[row2 + 1][col2 + 1] + sums[row1][col1] - sums[row2 + 1][col1] - sums[row1][col2 + 1];
        }
    }
}
