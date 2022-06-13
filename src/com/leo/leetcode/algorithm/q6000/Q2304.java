package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个下标从 0 开始的整数矩阵 grid ，矩阵大小为 m x n ，由从 0 到 m * n - 1 的不同整数组成。
 * 你可以在此矩阵中，从一个单元格移动到 下一行 的任何其他单元格。
 * 如果你位于单元格 (x, y) ，且满足 x < m - 1 ，你可以移动到 (x + 1, 0), (x + 1, 1), ..., (x + 1, n - 1) 中的任何一个单元格。
 * 注意： 在最后一行中的单元格不能触发移动。
 * 每次可能的移动都需要付出对应的代价，代价用一个下标从 0 开始的二维数组 moveCost 表示，该数组大小为 (m * n) x n ，其中 moveCost[i][j] 是从值为 i 的单元格移动到下一行第 j 列单元格的代价。
 * 从 grid 最后一行的单元格移动的代价可以忽略。
 * grid 一条路径的代价是：所有路径经过的单元格的 值之和 加上 所有移动的 代价之和 。
 * 从 第一行 任意单元格出发，返回到达 最后一行 任意单元格的最小路径代价。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、2 <= m, n <= 50
 * 4、grid 由从 0 到 m * n - 1 的不同整数组成
 * 5、moveCost.length == m * n
 * 6、moveCost[i].length == n
 * 7、1 <= moveCost[i][j] <= 100
 * 链接：https://leetcode.cn/problems/minimum-path-cost-in-a-grid
 */
public class Q2304 {

    public static void main(String[] args) {
        // 17
        System.out.println(new Q2304().minPathCost(stringToInt2dArray("[[5,3],[4,0],[2,1]]"), stringToInt2dArray("[[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]")));
        // 6
        System.out.println(new Q2304().minPathCost(stringToInt2dArray("[[5,1,2],[4,0,3]]"), stringToInt2dArray(" [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]")));
    }

    public int minPathCost(int[][] grid, int[][] moveCost) {
        int m = grid.length, n = grid[0].length, ret = Integer.MAX_VALUE;
        int[][] dp = new int[m][n];
        System.arraycopy(grid[0], 0, dp[0], 0, n);
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = dp[i - 1][0] + grid[i][j] + moveCost[grid[i - 1][0]][j];
                for (int k = 1; k < n; k++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][k] + moveCost[grid[i - 1][k]][j] + grid[i][j]);
                }
            }
        }
        for (int v : dp[m - 1]) ret = Math.min(ret, v);
        return ret;
    }
}
