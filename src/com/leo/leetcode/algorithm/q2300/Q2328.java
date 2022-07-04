package com.leo.leetcode.algorithm.q2300;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 m x n 的整数网格图 grid ，你可以从一个格子移动到 4 个方向相邻的任意一个格子。
 * 请你返回在网格图中从 任意 格子出发，达到 任意 格子，且路径中的数字是 严格递增 的路径数目。由于答案可能会很大，请将结果对 10^9 + 7 取余 后返回。
 * 如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 1000
 * 4、1 <= m * n <= 10^5
 * 5、1 <= grid[i][j] <= 10^5
 * 链接：https://leetcode.cn/problems/number-of-increasing-paths-in-a-grid
 */
public class Q2328 {

    public static void main(String[] args) {
        // 8
        System.out.println(new Q2328().countPaths(stringToInt2dArray("[[1,1],[3,4]]")));
        // 3
        System.out.println(new Q2328().countPaths(stringToInt2dArray("[[1],[2]]")));
    }

    int MOD = 1_000_000_007, m, n;
    // 方向数组
    int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int countPaths(int[][] grid) {
        m = grid.length;
        n = grid[0].length;
        this.mem = new int[m][n];
        for (int[] line : mem) Arrays.fill(line, -1);
        long ret = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ret = (ret + bfs(grid, i, j, 0)) % MOD;
            }
        }
        return (int) ret;
    }

    int[][] mem;

    int bfs(int[][] grid, int x, int y, int v) {
        if (x < 0 || x > m - 1 || y < 0 || y > n - 1) return 0;
        if (grid[x][y] <= v) return 0;
        if (mem[x][y] != -1) return mem[x][y];
        long ret = 1;
        for (int[] dir : dirs) {
            ret = (ret + bfs(grid, x + dir[0], y + dir[1], grid[x][y])) % MOD;
        }
        mem[x][y] = (int) ret;
        return (int) ret;
    }
}
