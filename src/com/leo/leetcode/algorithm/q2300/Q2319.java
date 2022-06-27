package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 如果一个正方形矩阵满足下述 全部 条件，则称之为一个 X 矩阵 ：
 * 1、矩阵对角线上的所有元素都 不是 0
 * 2、矩阵中所有其他元素都是 0
 * 给你一个大小为 n x n 的二维整数数组 grid ，表示一个正方形矩阵。如果 grid 是一个 X 矩阵 ，返回 true ；否则，返回 false 。
 * 提示：
 * 1、n == grid.length == grid[i].length
 * 2、3 <= n <= 100
 * 3、0 <= grid[i][j] <= 10^5
 * 链接：https://leetcode.cn/problems/check-if-matrix-is-x-matrix
 */
public class Q2319 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q2319().checkXMatrix(stringToInt2dArray("[[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]")));
        // false
        System.out.println(new Q2319().checkXMatrix(stringToInt2dArray("[[5,7,0],[0,3,1],[0,5,0]]")));
    }

    public boolean checkXMatrix(int[][] grid) {
        int n = grid.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j || i == n - 1 - j) {
                    if (grid[i][j] == 0) {
                        return false;
                    }
                } else {
                    if (grid[i][j] != 0) return false;
                }
            }
        }
        return true;
    }
}
