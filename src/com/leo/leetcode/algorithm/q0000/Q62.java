package com.leo.leetcode.algorithm.q0000;

/**
 * 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
 * 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
 * 问总共有多少条不同的路径？
 * 链接：https://leetcode-cn.com/problems/unique-paths
 */
public class Q62 {
    public static void main(String[] args) {
        new Q62().TestOJ();
    }

    public void TestOJ() {
        System.out.println(uniquePaths(3, 2)); // 3
        System.out.println(uniquePaths(7, 3)); // 28
    }

    public int uniquePaths(int m, int n) {
        if (m <= 1 || n <= 1) return 1;
        int[] arr = new int[m];
        for (int i = 0; i < m; i++) arr[i] = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                arr[j] += arr[j - 1];
            }
        }
        return arr[m - 1];
    }


}
