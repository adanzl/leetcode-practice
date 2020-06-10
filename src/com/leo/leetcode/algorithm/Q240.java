package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q240 {
    public void TestOJ() {
        int[][] matrix = LCUtil.stringToInt2dArray("["
                + "[ 1,  4,  7, 11, 15],"
                + "[ 2,  5,  8, 12, 19],"
                + "[ 3,  6,  9, 16, 22],"
                + "[10, 13, 14, 17, 24],"
                + "[18, 21, 23, 26, 30]"
                + "]"
        );
        System.out.println(searchMatrix(matrix, 5)); // t
        System.out.println(searchMatrix(matrix, 20)); // f
    }


    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0) return false;
        // 起点为最右上角的元素
        int row = 0, col = matrix[0].length - 1;
        // 判断当前数组元素和target，如果当前大于target，往左走；小与target，往下走
        while (row < matrix.length && col >= 0) {
            if (matrix[row][col] < target) {
                row++;
            } else if (matrix[row][col] > target) {
                col--;
            } else {
                return true;
            }
        }

        return false;
    }

}
