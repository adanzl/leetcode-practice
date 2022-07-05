package com.leo.leetcode.lcp;

import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2的多米诺骨牌，
 * 你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。
 * 输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。
 * 输出：一个整数，代表最多能在棋盘上放的骨牌数。
 * 限制：
 * 1、1 <= n <= 8
 * 2、1 <= m <= 8
 * 3、0 <= b <= n * m
 * 链接：https://leetcode.cn/problems/broken-board-dominoes
 */
public class LCP04 {

    public static void main(String[] args) {
        // 23
        System.out.println(new LCP04().domino(8, 8, stringToInt2dArray("[[1, 0], [2, 5], [3, 1], [3, 2], [3, 4], [4, 0], [4, 3], [4, 6], [4, 7], [5, 3], [5, 5], [5, 6], [6, 3], [7, 2], [7, 7]]")));
        // 4
        System.out.println(new LCP04().domino(3, 3, stringToInt2dArray("[]")));
        // 32
        System.out.println(new LCP04().domino(8, 8, stringToInt2dArray("[]")));
        // 12
        System.out.println(new LCP04().domino(5, 5, stringToInt2dArray("[]")));
        // 2
        System.out.println(new LCP04().domino(2, 3, stringToInt2dArray("[[1, 0], [1, 1]]")));
    }

    int n, m;
    Map<Long, Integer> mem = new HashMap<>();
    int[][] dirs = {{0, 1}, {1, 0}};

    public int domino(int n, int m, int[][] broken) {
        this.n = n;
        this.m = m;
        int[][] grid = new int[n][m];
        for (int[] br : broken) grid[br[0]][br[1]] = 2;
        return dfs(grid, 0, 0);
    }

    int dfs(int[][] grid, int idx, long sign) {
        int size = m * n, i = idx / m, j = idx % m;
        if (idx > size - 1) return 0;
        if (mem.containsKey(sign)) return mem.get(sign);
        boolean skip = true;
        int ret = 0;
        if (grid[i][j] == 0) {
            grid[i][j] = 1;
            for (int[] dir : dirs) {
                int x = i + dir[0], y = j + dir[1];
                if (x >= n || y >= m || grid[x][y] != 0) continue;
                grid[x][y] = 1;
                long newSign = sign | (1L << idx) | (1L << (x * m + y));
                ret = Math.max(ret, dfs(grid, idx + dir[1] + 1, newSign) + 1);
                grid[x][y] = 0;
                skip = false;
            }
            grid[i][j] = 0;
        }
        if (skip) ret = dfs(grid, idx + 1, sign);
        mem.put(sign, ret);
        return ret;
    }
}
