package com.leo.leetcode.lcci;

public class Q0811 {

    public static void main(String[] args) {
        System.out.println(new Q0811().waysToChange(10)); // 4
        System.out.println(new Q0811().waysToChange(5)); // 2
    }

    public int waysToChange(int n) {
        long[] marks = new long[n + 1];
        marks[0] = 1;
        int[] coins = new int[]{1, 5, 10, 25};
        for (int c : coins) {
            for (int i = c; i <= n; i++) {
                marks[i] += marks[i - c];
            }
        }
        return (int) (marks[n] % 1000000007);
    }
}
