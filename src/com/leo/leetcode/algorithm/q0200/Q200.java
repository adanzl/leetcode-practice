package com.leo.leetcode.algorithm.q0200;

/**
 * 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
 * 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
 * 此外，你可以假设该网格的四条边均被水包围。
 * <p>
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 300
 * 4、grid[i][j] 的值为 '0' 或 '1'
 * <p>
 * 链接：https://leetcode-cn.com/problems/number-of-islands
 */
public class Q200 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q200().numIslands(new char[][]{
                {'1', '1', '1', '1', '0'},
                {'1', '1', '0', '1', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '0', '0', '0'}}));
        // 3
        System.out.println(new Q200().numIslands(new char[][]{
                {'1', '1', '0', '0', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '1', '0', '0'},
                {'0', '0', '0', '1', '1'}}));
    }

    // walk: s[i] != 0 -> check
    public int numIslands(char[][] grid) {
        int ret = 0;
        for (int x = 0; x < grid.length; x++) {
            for (int y = 0; y < grid[x].length; y++) {
                if (grid[x][y] == 1) {
                    continue;
                }
                if (grid[x][y] == '1') {
                    ret++;
                    expand(grid, x, y);
                }
            }
        }
        return ret;
    }

    // up down left right expand one time
    void expand(char[][] grid, int x, int y) {
        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] == '0' || grid[x][y] == 1) return;
        grid[x][y] = 1;
        expand(grid, x - 1, y);
        expand(grid, x + 1, y);
        expand(grid, x, y - 1);
        expand(grid, x, y + 1);
    }
}
