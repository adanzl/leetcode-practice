package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 一个N x N的网格(grid) 代表了一块樱桃地，每个格子由以下三种数字的一种来表示：
 * 1、0 表示这个格子是空的，所以你可以穿过它。
 * 2、1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
 * 3、-1 表示这个格子里有荆棘，挡着你的路。
 * 你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：
 * 1、从位置 (0, 0) 出发，最后到达 (N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；
 * 2、当到达 (N-1, N-1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
 * 3、当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；
 * 4、如果在 (0, 0) 和 (N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。
 * 说明:
 * 1、grid 是一个 N * N 的二维数组，N的取值范围是1 <= N <= 50。
 * 2、每一个 grid[i][j] 都是集合 {-1, 0, 1}其中的一个数。
 * 3、可以保证起点 grid[0][0] 和终点 grid[N-1][N-1] 的值都不会是 -1。
 * 链接：https://leetcode.cn/problems/cherry-pickup
 */
public class Q741 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q741().cherryPickup(stringToInt2dArray("[[0,1,-1],[1,0,-1],[1,1,1]]")));
    }

    int[][] grid;
    Integer[][][][] dp;
    int[][] dirs = new int[][]{{0, 1}, {1, 0}};
    int N;

    public int cherryPickup(int[][] grid) {
        N = grid.length;
        this.grid = grid;
        this.dp = new Integer[N][N][N][N];
        dp[N - 1][N - 1][N - 1][N - 1] = grid[N - 1][N - 1];
        return Math.max(0, dfs(0, 0, 0, 0));
    }

    // x0 + y0 == x1 + y1
    int dfs(int x0, int y0, int x1, int y1) {
        if (x0 >= N || y0 >= N || x1 >= N || y1 >= N || grid[x0][y0] == -1 || grid[x1][y1] == -1)
            return Integer.MIN_VALUE / 2;
        if (dp[x0][y0][x1][y1] != null) return dp[x0][y0][x1][y1];
        int ret = Integer.MIN_VALUE;
        for (int[] dir0 : dirs) {
            int nx0 = x0 + dir0[0], ny0 = y0 + dir0[1];
            for (int[] dir1 : dirs) {
                int nx1 = x1 + dir1[0], ny1 = y1 + dir1[1];
                ret = Math.max(ret, dfs(nx0, ny0, nx1, ny1));
            }
        }
        ret += grid[x0][y0];
        if (x0 != x1 || y0 != y1) {
            ret += grid[x1][y1];
        }
        this.dp[x0][y0][x1][y1] = ret;
        return ret;
    }
}
