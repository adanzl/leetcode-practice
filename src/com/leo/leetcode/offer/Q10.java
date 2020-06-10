package com.leo.leetcode.offer;

public class Q10 {

    public static void main(String[] args) {
        System.out.println(new Q10().fib(100)); //
    }

    public int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        int[] arr = new int[3];
        arr[2] = 1;
        for (int i = 2; i <= n; i++) {
            arr[0] = arr[1];
            arr[1] = arr[2];
            arr[2] = (arr[0] + arr[1]) % 1000000007;
        }

        return arr[2];
    }
}
