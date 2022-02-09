package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 二维矩阵 grid由 0（土地）和 1（水）组成。岛是由最大的4个方向连通的 0组成的群，封闭岛是一个完全 由1包围（左、上、右、下）的岛。
 * 请返回 封闭岛屿 的数目。
 * 提示：
 * 1、1 <= grid.length, grid[0].length <= 100
 * 2、0 <= grid[i][j] <=1
 * 链接：https://leetcode-cn.com/problems/number-of-closed-islands
 */
public class Q1254 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1254().closedIsland(stringToInt2dArray("[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]")));
        // 1
        System.out.println(new Q1254().closedIsland(stringToInt2dArray("[[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]")));
        // 2
        System.out.println(new Q1254().closedIsland(stringToInt2dArray("[[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]")));
    }

    public int closedIsland(int[][] grid) {
        int ret = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        for (int i = 0; i < grid[0].length; i++) {
            if (!visited[0][i]) expand(grid, visited, 0, i);
            if (!visited[grid.length - 1][i]) expand(grid, visited, grid.length - 1, i);
        }
        for (int i = 0; i < grid.length; i++) {
            if (!visited[i][0]) expand(grid, visited, i, 0);
            if (!visited[i][grid[0].length - 1]) expand(grid, visited, i, grid[0].length - 1);
        }
        for (int i = 1; i < grid.length - 1; i++) {
            for (int j = 1; j < grid[0].length - 1; j++) {
                if (visited[i][j] || grid[i][j] == 1) continue;
                expand(grid, visited, i, j);
                ++ret;
            }
        }
        return ret;
    }

    void expand(int[][] grid, boolean[][] visited, int x, int y) {
        visited[x][y] = true;
        if (grid[x][y] == 1) return;
        if (x > 0 && !visited[x - 1][y]) expand(grid, visited, x - 1, y);
        if (x < grid.length - 1 && !visited[x + 1][y]) expand(grid, visited, x + 1, y);
        if (y > 0 && !visited[x][y - 1]) expand(grid, visited, x, y - 1);
        if (y < grid[0].length - 1 && !visited[x][y + 1]) expand(grid, visited, x, y + 1);
    }
}
