package com.leo.leetcode.algorithm.q0400;

import java.util.Comparator;
import java.util.PriorityQueue;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
 * 提示:
 * 1、m == heightMap.length
 * 2、n == heightMap[i].length
 * 3、1 <= m, n <= 200
 * 4、0 <= heightMap[i][j] <= 2 * 10^4
 * 链接：https://leetcode.cn/problems/trapping-rain-water-ii
 */
public class Q407 {

    public static void main(String[] args) {
        // 14
        System.out.println(new Q407().trapRainWater(stringToInt2dArray("[[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]")));
        // 4
        System.out.println(new Q407().trapRainWater(stringToInt2dArray("[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]")));
        // 10
        System.out.println(new Q407().trapRainWater(stringToInt2dArray("[[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]")));
    }

    public int trapRainWater(int[][] heightMap) {
        int m = heightMap.length, n = heightMap[0].length, ret = 0;
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        boolean[][] visited = new boolean[m][n];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        for (int i = 0; i < m; i++) {
            pq.add(new int[]{heightMap[i][0], i, 0});
            pq.add(new int[]{heightMap[i][n - 1], i, n - 1});
            visited[i][0] = true;
            visited[i][n - 1] = true;
        }
        for (int i = 0; i < n; i++) {
            pq.add(new int[]{heightMap[0][i], 0, i});
            pq.add(new int[]{heightMap[m - 1][i], m - 1, i});
            visited[0][i] = true;
            visited[m - 1][i] = true;
        }
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int h = cur[0], x = cur[1], y = cur[2];
            if (h == 0) continue;
            for (int[] dir : dirs) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n || visited[nx][ny]) continue;
                visited[nx][ny] = true;
                ret += Math.max(0, h - heightMap[nx][ny]);
                pq.add(new int[]{Math.max(h, heightMap[nx][ny]), nx, ny});
            }
        }
        return ret;
    }
}
