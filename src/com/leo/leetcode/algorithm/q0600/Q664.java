package com.leo.leetcode.algorithm.q0600;

/**
 * 有台奇怪的打印机有以下两个特殊要求：
 * 打印机每次只能打印由 同一个字符 组成的序列。
 * 每次可以在从起始到结束的任意位置打印新字符，并且会覆盖掉原来已有的字符。
 * 给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。
 * 链接：https://leetcode.cn/problems/strange-printer
 */
public class Q664 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q664().strangePrinter("aaabbb"));
        // 2
        System.out.println(new Q664().strangePrinter("aba"));
    }

    public int strangePrinter(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
            for (int j = i - 1; j >= 0; j--) {
                dp[j][i] = n;
                if (s.charAt(i) == s.charAt(j)) dp[j][i] = dp[j + 1][i];
                else {
                    for (int k = j; k < i; k++) {
                        dp[j][i] = Math.min(dp[j][i], dp[j][k] + dp[k + 1][i]);
                    }
                }
            }
        }
        return dp[0][n - 1];
    }
}
