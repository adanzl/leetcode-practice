package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

import java.util.*;

/**
 * 给你一个下标从 0 开始的二维整数数组 grid ，数组大小为 m x n 。每个单元格都是两个值之一：
 * 1、0 表示一个 空 单元格，
 * 2、1 表示一个可以移除的 障碍物 。
 * 你可以向上、下、左、右移动，从一个空单元格移动到另一个空单元格。
 * 现在你需要从左上角 (0, 0) 移动到右下角 (m - 1, n - 1) ，返回需要移除的障碍物的 最小 数目。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 10^5
 * 4、2 <= m * n <= 10^5
 * 5、grid[i][j] 为 0 或 1
 * 6、grid[0][0] == grid[m - 1][n - 1] == 0
 * 链接：https://leetcode.cn/problems/minimum-obstacle-removal-to-reach-corner
 */
public class Q2290 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q2290().minimumObstacles(stringToInt2dArray("[[0,0,1,1,1,1,0,0,0,1],[0,1,1,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,0],[0,0,1,1,1,1,0,0,1,1],[1,0,1,0,0,0,1,1,1,0]]")));
        // 0
        System.out.println(new Q2290().minimumObstacles(stringToInt2dArray("[[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]")));
        // 2
        System.out.println(new Q2290().minimumObstacles(stringToInt2dArray("[[0,1,1],[1,1,0],[1,1,0]]")));
    }

    public int minimumObstacles(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] dist = dijkstra(m, n, grid);
        return dist[dist.length - 1];
    }

    int[] dijkstra(int m, int n, int[][] grid) {
        int[] dist = new int[n * m];
        int[][] directions = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        boolean[] vis = new boolean[n * m];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        q.offer(new int[]{0, grid[0][0]});
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int minNext = cur[1], maxIdx = cur[0];
            if (vis[maxIdx]) continue;
            for (int[] dir : directions) {
                int x = maxIdx / n + dir[0], y = maxIdx % n + dir[1];
                if (x < 0 || x >= m || y < 0 || y >= n) continue;
                int nextIdx = x * n + y;
                int nextVal = grid[nextIdx / n][nextIdx % n];
                if (nextVal + minNext < dist[nextIdx]) {
                    dist[nextIdx] = nextVal + minNext;
                    q.offer(new int[]{nextIdx, dist[nextIdx]});
                }
            }
            vis[maxIdx] = true;
        }
        return dist;
    }

}
