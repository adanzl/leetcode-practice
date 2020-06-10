package com.leo.leetcode.algorithm;

import org.junit.Test;

public class Q64 {
    @Test
    public void TestOJ() {
        System.out.println(minPathSum(new int[][]{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}})); // 7
    }

    public int minPathSum(int[][] grid) {
        if (grid.length == 0) return 0;
        int[] arr = new int[grid[0].length];
        arr[0] = grid[0][0];
        for (int i = 1; i < arr.length; i++) arr[i] = arr[i - 1] + grid[0][i];

        for (int i = 1; i < grid.length; i++) {
            arr[0] += grid[i][0];
            for (int j = 1; j < grid[0].length; j++) {
                arr[j] = Math.min(arr[j - 1], arr[j]) + grid[i][j];
            }
        }
        return arr[arr.length - 1];
    }
}
