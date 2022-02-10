package com.leo.leetcode.algorithm.q1000;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
 * 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
 * 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 500
 * 4、grid[i][j] 的值为 0 或 1
 * <p>
 * 链接：https://leetcode-cn.com/problems/number-of-enclaves
 */
public class Q1020 {

    public static void main(String[] args) {
        //
        System.out.println(new Q1020().numEnclaves(stringToInt2dArray("[[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]")));
        // 3
        System.out.println(new Q1020().numEnclaves(stringToInt2dArray("[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]")));
        // 0
        System.out.println(new Q1020().numEnclaves(stringToInt2dArray("[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]")));
    }

    public int numEnclaves(int[][] grid) {
        int ret = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        for (int i = 0; i < grid[0].length; i++) {
            if (grid[0][i] == 1) expand(grid, visited, 0, i);
            if (grid[grid.length - 1][i] == 1) expand(grid, visited, grid.length - 1, i);
        }
        for (int i = 0; i < grid.length; i++) {
            if (grid[i][0] == 1) expand(grid, visited, i, 0);
            if (grid[i][grid[0].length - 1] == 1) expand(grid, visited, i, grid[0].length - 1);
        }
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) ++ret;
            }
        }
        return ret;
    }

    void expand(int[][] grid, boolean[][] visited, int x, int y) {
        if (x < 0 || x > grid.length - 1 || y < 0 || y > grid[0].length - 1 || visited[x][y]) return;
        visited[x][y] = true;
        if (grid[x][y] == 0) return;
        expand(grid, visited, x - 1, y);
        expand(grid, visited, x + 1, y);
        expand(grid, visited, x, y - 1);
        expand(grid, visited, x, y + 1);
    }
}
