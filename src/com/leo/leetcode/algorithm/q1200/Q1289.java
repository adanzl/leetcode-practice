package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 n x n 整数矩阵 arr ，请你返回 非零偏移下降路径 数字和的最小值。
 * 非零偏移下降路径 定义为：从 arr 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。
 * 提示：
 * 1、n == grid.length == grid[i].length
 * 2、1 <= n <= 200
 * 3、-99 <= grid[i][j] <= 99
 * 链接：https://leetcode-cn.com/problems/minimum-falling-path-sum-ii
 */
public class Q1289 {

    public static void main(String[] args) {
        // 10
        System.out.println(new Q1289().minFallingPathSum(stringToInt2dArray("[[1,2,3,4],[4,5,1,7],[7,8,9,1],[7,8,9,10]]")));
        // 13
        System.out.println(new Q1289().minFallingPathSum(stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]")));
        // 7
        System.out.println(new Q1289().minFallingPathSum(stringToInt2dArray("[[7]]")));
    }

    public int minFallingPathSum(int[][] grid) {
        int ret1 = 0, ret2 = ret1, idx1 = -1, n = grid.length, INF = 300000;
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            int min1 = INF, min2 = min1, mi1 = -1;
            for (int j = 0; j < n; j++) {
                dp[i][j] = (idx1 == j ? ret2 : ret1) + grid[i][j];
                if (dp[i][j] < min1) {
                    min2 = min1;
                    min1 = dp[i][j];
                    mi1 = j;
                } else if(dp[i][j] < min2) min2 = dp[i][j];
            }
            ret1 = min1;
            ret2 = min2;
            idx1 = mi1;
        }
        return ret1;
    }
}
