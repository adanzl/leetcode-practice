package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
 * 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
 * <p>
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、1 <= m, n <= 20
 * 4、0 <= matrix[i][j] <= 99
 * <p>
 * 进阶：
 * 1、如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？
 * 2、如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？
 * <p>
 * 链接：https://leetcode-cn.com/problems/toeplitz-matrix
 */
public class Q766 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q766().isToeplitzMatrix(stringToInt2dArray("[[1,2,3,4],[5,1,2,3],[9,5,1,2]]")));
        // false
        System.out.println(new Q766().isToeplitzMatrix(stringToInt2dArray("[[1,2],[2,2]]")));
    }

    public boolean isToeplitzMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (i > j) {
                    if (matrix[i - j][0] != matrix[i][j]) return false;
                } else {
                    if (matrix[0][j - i] != matrix[i][j]) return false;
                }

            }
        }
        return true;
    }
}
