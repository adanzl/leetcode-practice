package com.leo.leetcode.algorithm.q1900;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你两个m x n的二进制矩阵grid1 和grid2，它们只包含0（表示水域）和 1（表示陆地）。
 * 一个 岛屿是由 四个方向（水平或者竖直）上相邻的1组成的区域。任何矩阵以外的区域都视为水域。
 * 如果 grid2的一个岛屿，被 grid1的一个岛屿完全 包含，也就是说 grid2中该岛屿的每一个格子都被 grid1中同一个岛屿完全包含，
 * 那么我们称 grid2中的这个岛屿为 子岛屿。
 * 请你返回 grid2中 子岛屿的 数目。
 * 提示：
 * 1、m == grid1.length == grid2.length
 * 2、n == grid1[i].length == grid2[i].length
 * 3、1 <= m, n <= 500
 * 4、grid1[i][j] 和grid2[i][j]都要么是0要么是1。
 * <p>
 * 链接：https://leetcode-cn.com/problems/count-sub-islands
 */
public class Q1905 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1905().countSubIslands(
                stringToInt2dArray("[[0,1,1,1,1,1,1,0,1,1],[1,0,1,1,1,0,1,1,1,1],[1,0,1,1,0,1,1,1,1,1],[1,0,1,1,0,1,1,1,1,1],[1,0,1,1,1,1,1,0,1,1],[1,1,0,0,1,1,1,0,0,1],[1,1,0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,1,1,1],[1,0,0,1,1,0,1,1,1,1]]"),
                stringToInt2dArray("[[0,0,1,1,1,1,1,1,1,1],[1,0,0,1,1,1,0,0,1,0],[1,1,1,0,1,1,0,1,1,1],[1,0,0,1,0,0,1,0,1,1],[0,1,1,1,0,1,0,1,1,0],[1,1,1,0,0,0,1,0,1,0],[1,1,1,1,1,1,1,1,1,1],[1,1,1,0,0,0,1,0,1,1],[1,1,1,1,1,1,0,1,1,0]]")));
        // 2
        System.out.println(new Q1905().countSubIslands(
                stringToInt2dArray("[[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]"),
                stringToInt2dArray("[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]")));
        // 3
        System.out.println(new Q1905().countSubIslands(
                stringToInt2dArray("[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]"),
                stringToInt2dArray("[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]")));
    }

    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int w1 = grid1.length, h1 = grid1[0].length, w2 = grid2.length, h2 = grid2[0].length;
        boolean[][] visited1 = new boolean[w1][h1], visited2 = new boolean[w2][h2];
        int[] parent = new int[w1 * h1];
        for (int i = 0; i < parent.length; i++) parent[i] = i;
        for (int i = 0; i < w1; i++) {
            for (int j = 0; j < h1; j++) {
                if (grid1[i][j] == 1 && !visited1[i][j]) expand(grid1, visited1, parent, i, j, i, j);
            }
        }
        int ret = 0;
        for (int i = 0; i < grid2.length; i++) {
            for (int j = 0; j < grid2[i].length; j++) {
                if (grid1[i][j] == 1 && grid2[i][j] == 1 && !visited2[i][j] && check(grid2, visited2, i, j, parent, parent[i * h1 + j]))
                    ++ret;
            }
        }
        return ret;
    }

    int find(int[] parent, int len, int x, int y) {
        int idx = len * x + y, v = parent[idx];
        return v == idx ? idx : (parent[idx] = find(parent, len, v / len, v % len));
    }

    void merge(int[] parent, int len, int x0, int y0, int x1, int y1) {
        int p1 = find(parent, len, x0, y0), p2 = find(parent, len, x1, y1);
        if (p1 == p2) return;
        parent[p2] = p1;
    }

    void expand(int[][] grid, boolean[][] visited, int[] parent, int px, int py, int x, int y) {
        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || visited[x][y]) return;
        visited[x][y] = true;
        if (grid[x][y] == 0) return;
        merge(parent, grid[0].length, px, py, x, y);
        expand(grid, visited, parent, x, y, x, y + 1);
        expand(grid, visited, parent, x, y, x, y - 1);
        expand(grid, visited, parent, x, y, x + 1, y);
        expand(grid, visited, parent, x, y, x - 1, y);
    }

    boolean check(int[][] grid, boolean[][] visited, int x, int y, int[] parent, int pv) {
        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || visited[x][y]) return true;
        visited[x][y] = true;
        if (grid[x][y] == 0) return true;
        boolean ret = check(grid, visited, x - 1, y, parent, pv);
        ret &= check(grid, visited, x, y - 1, parent, pv);
        ret &= check(grid, visited, x + 1, y, parent, pv);
        ret &= check(grid, visited, x, y + 1, parent, pv);
        ret &= parent[x * grid[0].length + y] == pv;
        return ret;
    }
}
