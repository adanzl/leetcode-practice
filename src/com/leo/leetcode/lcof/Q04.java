package com.leo.leetcode.lcof;

import com.leo.utils.LCUtil;

public class Q04 {
    public static void main(String[] args) {
        System.out.println(new Q04().findNumberIn2DArray(LCUtil.stringToInt2dArray("[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]"), 5)); // true
        System.out.println(new Q04().findNumberIn2DArray(LCUtil.stringToInt2dArray("[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]"), 20)); // false
    }

    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) return false;
        int row = 0, col = matrix[0].length - 1;
        int d = 0; // 0 left, 1 down
        while (row < matrix.length && col >= 0) {
            if (matrix[row][col] == target) {
                return true;
            } else if (d == 0) {
                if (matrix[row][col] > target) {
                    col--;
                } else {
                    row++;
                    d = 1;
                }
            } else {
                if (matrix[row][col] < target) {
                    row++;
                } else {
                    col--;
                    d = 0;
                }
            }
        }
        return false;
    }
}
