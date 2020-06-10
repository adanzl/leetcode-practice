package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

/**
 * 在给定的网格中，每个单元格可以有以下三个值之一：
 * <p>
 * 值 0 代表空单元格；
 * 值 1 代表新鲜橘子；
 * 值 2 代表腐烂的橘子。
 * 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
 * <p>
 * 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
 * <p>
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/rotting-oranges
 */
public class Q994 {
    public static void main(String[] args) {
        new Q994().TestOJ();
    }

    public void TestOJ() {
        System.out.println(orangesRotting(LCUtil.stringToInt2dArray("[[2,1,1],[1,1,0],[0,1,1]]"))); // 4
    }

    public int orangesRotting(int[][] grid) {
        int freshCount, pre = -1, time = 0;
        while (true) {
            freshCount = getFreshCount(grid);
            if (freshCount == 0) return time;
            if (pre == freshCount) return -1;
            pre = freshCount;
            doChange(grid);
            time++;
        }
    }

    int getFreshCount(int[][] grid) {
        int freshCount = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 3) {
                    grid[i][j] = 2;
                }
                if (grid[i][j] == 1) {
                    freshCount++;
                }
            }
        }
        return freshCount;
    }

    void doChange(int[][] grid) {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 2) {
                    if (i > 0 && grid[i - 1][j] != 0) {
                        if (grid[i - 1][j] == 1) grid[i - 1][j] = 3;
                    }
                    if (i < grid.length - 1 && grid[i + 1][j] != 0) {
                        if (grid[i + 1][j] == 1) grid[i + 1][j] = 3;
                    }
                    if (j > 0 && grid[i][j - 1] != 0) {
                        if (grid[i][j - 1] == 1) grid[i][j - 1] = 3;
                    }
                    if (j < grid[i].length - 1 && grid[i][j + 1] != 0) {
                        if (grid[i][j + 1] == 1) grid[i][j + 1] = 3;
                    }
                }
            }
        }
    }
}
