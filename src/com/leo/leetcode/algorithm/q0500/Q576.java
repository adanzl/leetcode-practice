package com.leo.leetcode.algorithm.q0500;

/**
 * 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。
 * 你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。
 * 给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。
 * 因为答案可能非常大，返回对 10^9 + 7 取余 后的结果。
 * 提示：
 * 1、1 <= m, n <= 50
 * 2、0 <= maxMove <= 50
 * 3、0 <= startRow < m
 * 4、0 <= startColumn < n
 * 链接：https://leetcode-cn.com/problems/out-of-boundary-paths
 */
public class Q576 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q576().findPaths(10, 10, 0, 5, 5));
        // 12
        System.out.println(new Q576().findPaths(1, 3, 3, 0, 1));
        // 6
        System.out.println(new Q576().findPaths(2, 2, 2, 0, 0));
    }

    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        if (maxMove == 0) return 0;
        int MOD = 1_000_000_007, ret = 0;
        int[][][] dp = new int[maxMove + 1][m][n];
        for (int i = 0; i < m; i++) {
            dp[1][i][0]++;
            dp[1][i][n - 1]++;
        }
        for (int i = 0; i < n; i++) {
            dp[1][0][i]++;
            dp[1][m - 1][i]++;
        }
        for (int i = 2; i <= maxMove; i++) {
            for (int row = 0; row < m; row++) {
                for (int col = 0; col < n; col++) {
                    if (row > 0) dp[i][row][col] = (dp[i][row][col] + dp[i - 1][row - 1][col]) % MOD;
                    if (row < m - 1) dp[i][row][col] = (dp[i][row][col] + dp[i - 1][row + 1][col]) % MOD;
                    if (col > 0) dp[i][row][col] = (dp[i][row][col] + dp[i - 1][row][col - 1]) % MOD;
                    if (col < n - 1) dp[i][row][col] = (dp[i][row][col] + dp[i - 1][row][col + 1]) % MOD;
                }
            }
        }
        for (int i = 1; i <= maxMove; i++) ret = (ret + dp[i][startRow][startColumn]) % MOD;
        return ret;
    }
}
