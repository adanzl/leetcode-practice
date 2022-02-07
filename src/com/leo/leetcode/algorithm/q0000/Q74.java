package com.leo.leetcode.algorithm.q0000;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
 * 每行中的整数从左到右按升序排列。
 * 每行的第一个整数大于前一行的最后一个整数。
 * 链接：https://leetcode-cn.com/problems/search-a-2d-matrix
 */
public class Q74 {
    public static void main(String[] args) {
        System.out.println(new Q74().searchMatrix(stringToInt2dArray("[[1]]"), 0)); // false
        System.out.println(new Q74().searchMatrix(stringToInt2dArray("[[1,3,5,7],[10,11,16,20],[23,30,34,50]]"), 3)); // true
        System.out.println(new Q74().searchMatrix(stringToInt2dArray("[[1,3,5,7],[10,11,16,20],[23,30,34,50]]"), 13)); // false
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length < 1) return false;
        int i = 0, j = matrix[0].length - 1;
        while (i < matrix.length && j >= 0) {
            if (matrix[i][j] == target) return true;
            else if (target < matrix[i][j]) j--;
            else if (target > matrix[i][j]) {
                if (j == matrix[0].length - 1) i++;
                else return false;
            }
        }
        return false;
    }
}
