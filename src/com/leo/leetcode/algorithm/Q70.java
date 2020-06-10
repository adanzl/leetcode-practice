package com.leo.leetcode.algorithm;

public class Q70 {
    public void TestOJ() {
        System.out.println(climbStairs(2)); // 2
        System.out.println(climbStairs(3)); // 3
        System.out.println(climbStairs(4)); // 5
    }

    public int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        int[] arr = new int[3];
        arr[0] = 1;
        arr[1] = 2;
        for (int i = 2; i < n; i++) {
            arr[2] = arr[0] + arr[1];
            arr[0] = arr[1];
            arr[1] = arr[2];
        }
        return arr[2];
    }
}
