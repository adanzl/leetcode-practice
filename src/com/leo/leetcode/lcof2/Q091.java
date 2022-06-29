package com.leo.leetcode.lcof2;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
 * 当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵 costs 来表示的。
 * 例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。
 * 请计算出粉刷完所有房子最少的花费成本。
 * 提示:
 * 1、costs.length == n
 * 2、costs[i].length == 3
 * 3、1 <= n <= 100
 * 4、1 <= costs[i][j] <= 20
 * 链接：https://leetcode.cn/problems/JEj789
 */
public class Q091 {

    public static void main(String[] args) {
        // 10
        System.out.println(new Q091().minCost(stringToInt2dArray("[[17,2,17],[16,16,5],[14,3,19]]")));
        // 2
        System.out.println(new Q091().minCost(stringToInt2dArray("[[7,6,2]]")));
    }

    public int minCost(int[][] costs) {
        int ret = Integer.MAX_VALUE, n = costs.length;
        int[][] dp = new int[n][3];
        dp[0] = costs[0];
        for (int i = 1; i < n; i++) {
            dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0];
            dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1];
            dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2];
        }
        for (int v : dp[n - 1]) ret = Math.min(ret, v);
        return ret;
    }
}
