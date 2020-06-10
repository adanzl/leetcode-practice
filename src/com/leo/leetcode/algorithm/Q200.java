package com.leo.leetcode.algorithm;

public class Q200 {
    public void TestOJ() {
        System.out.println(numIslands(new char[][]{
                {'1', '1', '1', '1', '0'},
                {'1', '1', '0', '1', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '0', '0', '0'}})); // 1
        System.out.println(numIslands(new char[][]{
                {'1', '1', '0', '0', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '1', '0', '0'},
                {'0', '0', '0', '1', '1'}})); // 3
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
