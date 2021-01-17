package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.LCUtil;

import java.util.HashSet;
import java.util.Set;

/**
 * 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
 * 进阶:
 * 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
 * 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
 * 你能想出一个常数空间的解决方案吗？
 * 链接：https://leetcode-cn.com/problems/set-matrix-zeroes
 * ！！！！！！！！ 这个题目无法实现方法三！！！！！！！！！
 */
public class Q73 {

    public static void main(String[] args) {
        int[][] matrix;
        matrix = LCUtil.stringToInt2dArray("[[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]");
        new Q73().setZeroes(matrix);
        System.out.println(LCUtil.int2dArrayToString(matrix)); // [[0,0,0,0,0],[0,0,0,0,0],[2147483647,2,-9,-6,0]]
        // ==============================================
        matrix = LCUtil.stringToInt2dArray("[[0,1,2,0],[3,4,5,2],[1,3,1,5]]");
        new Q73().setZeroes(matrix);
        System.out.println(LCUtil.int2dArrayToString(matrix)); // [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        // ==============================================
        matrix = LCUtil.stringToInt2dArray("[[1,1,1],[1,0,1],[1,1,1]]");
        new Q73().setZeroes(matrix);
        System.out.println(LCUtil.int2dArrayToString(matrix)); // [[1,0,1],[0,0,0],[1,0,1]]
        // ==============================================
    }

    public void setZeroes(int[][] matrix) {
        int R = matrix.length;
        int C = matrix[0].length;
        Set<Integer> rows = new HashSet<>();
        Set<Integer> cols = new HashSet<>();
        // Essentially, we mark the rows and columns that are to be made zero
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (matrix[i][j] == 0) {
                    rows.add(i);
                    cols.add(j);
                }
            }
        }
        // Iterate over the array once again and using the rows and cols sets, update the elements.
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (rows.contains(i) || cols.contains(j)) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
