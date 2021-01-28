package com.leo.leetcode.algorithm.q1600;

import static com.leo.utils.LCUtil.stringToInt2dArray;

public class Q1631 {

    public static void main(String[] args) {
        // 999999
        System.out.println(new Q1631().minimumEffortPath(stringToInt2dArray("[[1,1000000]]")));
        // 1
        System.out.println(new Q1631().minimumEffortPath(stringToInt2dArray("[[1,2,3],[3,8,4],[5,3,5]]")));
        // 2
        System.out.println(new Q1631().minimumEffortPath(stringToInt2dArray("[[1,2,2],[3,8,2],[5,3,5]]")));
        // 0
        System.out.println(new Q1631().minimumEffortPath(stringToInt2dArray("[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]")));
    }

    int rows;
    int cols;

    public int minimumEffortPath(int[][] heights) {
        rows = heights.length;
        cols = heights[0].length;
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}}; // 这个地方千万不要 new
        int l = 0, r = 1000000;
        while (l < r) {
            int mid = (l + r) / 2;
            if (dfs(heights, 0, 0, new boolean[rows][cols], mid, directions)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    boolean dfs(int[][] heights, int i, int j, boolean[][] marks, int limit, int[][] directions) {
        if (i == rows - 1 && j == cols - 1) return true;
        marks[i][j] = true;
        for (int[] d : directions) {
            int x = i + d[0], y = j + d[1];
            if (x < 0 || y < 0 || x >= rows || y >= cols || marks[x][y] || Math.abs(heights[x][y] - heights[i][j]) > limit)
                continue;
            if (dfs(heights, x, y, marks, limit, directions)) return true;
        }
        return false;
    }

}
