package com.leo.leetcode.algorithm.q0200;

import java.util.Arrays;

/**
 * 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、1 <= m, n <= 300
 * 4、matrix[i][j] 为 '0' 或 '1'
 * 链接：https://leetcode-cn.com/problems/maximal-square
 */
public class Q221 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q221().maximalSquare(
                new char[][]{
                        {'1', '0', '1', '0', '0'},
                        {'1', '0', '1', '1', '1'},
                        {'1', '1', '1', '1', '1'},
                        {'1', '0', '0', '1', '0'}}
                )
        );
    }

    /**
     * height{}: height{x} = row{x} == '1' ? (preHeight{x} + 1): 0 <br/>
     * left{}: left{x} = row{x} == '0' ? -1 : max(preLeft{x}, curLeft) <br/>
     * right{}: right{x} = row{x} == '0' ? len : min(preRight{x}, curRight)
     */
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 0)
            return 0;
        int maxArea = 0, len = matrix[0].length;
        int[] height = new int[len];
        int[] left = new int[len];
        int[] right = new int[len];
        Arrays.fill(right, len);

        for (char[] row : matrix) {
            int curLeft = -1, curRight = len;
            for (int j = 0; j < row.length; j++) {
                height[j] = row[j] == '1' ? height[j] + 1 : 0;
            }
            for (int j = 0; j < row.length; j++) {
                if (row[j] == '0') {
                    curLeft = j;
                    left[j] = -1;
                } else {
                    left[j] = Math.max(left[j], curLeft + 1);
                }
            }
            for (int j = row.length - 1; j >= 0; j--) {
                if (row[j] == '0') {
                    curRight = j;
                    right[j] = len;
                } else {
                    right[j] = Math.min(right[j], curRight);
                }
            }
            for (int j = 0; j < row.length; j++) {
                int width = Math.min(height[j], right[j] - left[j]);
                maxArea = Math.max(maxArea, width * width);
            }
        }
        return maxArea;
    }
}
