package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;

/**
 * 最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：
 * 1、Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
 * 2、Paste（粘贴）：粘贴 上一次 复制的字符。
 * 给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。
 * 提示：1 <= n <= 1000
 * 链接：https://leetcode.cn/problems/2-keys-keyboard
 */
public class Q650 {

    public static void main(String[] args) {
        // 21
        System.out.println(new Q650().minSteps(1000));
        // 17
        System.out.println(new Q650().minSteps(99));
        // 12
        System.out.println(new Q650().minSteps(50));
        // 3
        System.out.println(new Q650().minSteps(3));
        // 4
        System.out.println(new Q650().minSteps(4));
        // 0
        System.out.println(new Q650().minSteps(1));
    }

    public int minSteps(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, n + 1);
        dp[0] = 0;
        dp[1] = 0;
        for (int i = 1; i < n; i++) {
            int base = dp[i] + 1;
            for (int j = 1, idx = i + j * i; idx <= n; j++, idx = i + j * i) {
                dp[idx] = Math.min(dp[idx], base + j);
            }
        }
        return dp[n];
    }
}
