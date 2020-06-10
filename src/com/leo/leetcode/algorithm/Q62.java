package com.leo.leetcode.algorithm;

public class Q62 {
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
