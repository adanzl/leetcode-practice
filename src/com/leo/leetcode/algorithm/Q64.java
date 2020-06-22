package com.leo.leetcode.algorithm;

/**
 * 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
 * 说明：每次只能向下或者向右移动一步。
 * 链接：https://leetcode-cn.com/problems/minimum-path-sum/
 */
public class Q64 {
    public static void main(String[] args) {
        new Q64().TestOJ();
    }

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
