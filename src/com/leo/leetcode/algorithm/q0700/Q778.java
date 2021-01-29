package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。
 * 现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。
 * 你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。
 * 假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
 * 你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？
 * <p>
 * 提示:
 * 1、2 <= N <= 50.
 * 2、grid[i][j] 是 [0, ..., N*N - 1] 的排列。
 * <p>
 * 链接：https://leetcode-cn.com/problems/swim-in-rising-water
 */
public class Q778 {

    public static void main(String[] args) {
        // 14
        System.out.println(new Q778().swimInWater(stringToInt2dArray("[[9,5,7,2],[0,10,8,15],[1,4,3,12],[6,13,11,14]]")));
        // 3
        System.out.println(new Q778().swimInWater(stringToInt2dArray("[[3,2],[0,1]]")));
        // 3
        System.out.println(new Q778().swimInWater(stringToInt2dArray("[[0,2],[1,3]]")));
        // 16
        System.out.println(new Q778().swimInWater(stringToInt2dArray("[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]")));
    }

    int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int N;

    public int swimInWater(int[][] grid) {
        N = grid.length;
        int l = grid[0][0], r = N * N + 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (dfs(grid, 0, 0, new boolean[N][N], mid)) r = mid;
            else l = mid + 1;
        }
        return l;
    }

    boolean dfs(int[][] grid, int x, int y, boolean[][] marks, int t) {
        if (x == N - 1 && y == N - 1) return true;
        marks[x][y] = true;
        for (int[] d : directions) {
            int nx = x + d[0], ny = y + d[1];
            if (nx < 0 || ny < 0 || nx >= N || ny >= N || marks[nx][ny]
                    || grid[nx][ny] > t) continue;
            if (dfs(grid, nx, ny, marks, t)) return true;
        }
        return false;
    }
}
