package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。
 * 每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。
 * 为了使收益最大化，矿工需要按以下规则来开采黄金：
 * 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
 * 矿工每次可以从当前位置向上下左右四个方向走。
 * 每个单元格只能被开采（进入）一次。
 * 不得开采（进入）黄金数目为 0 的单元格。
 * 矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
 * <p>
 * 提示：
 * 1、1 <= grid.length, grid[i].length <= 15
 * 2、0 <= grid[i][j] <= 100
 * 3、最多 25 个单元格中有黄金。
 * <p>
 * 链接：https://leetcode-cn.com/problems/path-with-maximum-gold
 */
public class Q1219 {

    public static void main(String[] args) {
        // 24
        System.out.println(new Q1219().getMaximumGold(stringToInt2dArray("[[0,6,0],[5,8,7],[0,9,0]]")));
        // 28
        System.out.println(new Q1219().getMaximumGold(stringToInt2dArray("[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]")));
    }

    boolean[][] visited;
    int maxValue = 0, w, h;

    public int getMaximumGold(int[][] grid) {
        w = grid.length;
        h = grid[0].length;
        visited = new boolean[w][h];
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                dfs(grid, i, j, 0);
            }
        }
        return maxValue;
    }

    void dfs(int[][] grid, int x, int y, int v) {
        if (x < 0 || x >= w || y < 0 || y >= h || visited[x][y] || grid[x][y] == 0) return;
        visited[x][y] = true;
        v += grid[x][y];
        maxValue = Math.max(maxValue, v);
        dfs(grid, x + 1, y, v);
        dfs(grid, x - 1, y, v);
        dfs(grid, x, y + 1, v);
        dfs(grid, x, y - 1, v);
        visited[x][y] = false;
    }
}
