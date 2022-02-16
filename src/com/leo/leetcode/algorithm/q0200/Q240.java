package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;

/**
 * 编写一个高效的算法来搜索  m  x  n  矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
 * 1、每行的元素从左到右升序排列。
 * 2、每列的元素从上到下升序排列。
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、1 <= n, m <= 300
 * 4、-10^9  <= matrix[i][j] <= 10^9
 * 5、每行的所有元素从左到右升序排列
 * 6、每列的所有元素从上到下升序排列
 * 7、-10^9  <= target <= 10^9
 * 链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
 */
public class Q240 {
    public static void main(String[] args) {
        int[][] matrix = LCUtil.stringToInt2dArray("["
                + "[ 1,  4,  7, 11, 15],"
                + "[ 2,  5,  8, 12, 19],"
                + "[ 3,  6,  9, 16, 22],"
                + "[10, 13, 14, 17, 24],"
                + "[18, 21, 23, 26, 30]"
                + "]"
        );

        // true
        System.out.println(new Q240().searchMatrix(matrix, 5));
        // false
        System.out.println(new Q240().searchMatrix(matrix, 20));
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
