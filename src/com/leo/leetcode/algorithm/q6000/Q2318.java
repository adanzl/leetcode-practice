package com.leo.leetcode.algorithm.q6000;

/**
 * 给你一个整数 n 。你需要掷一个 6 面的骰子 n 次。请你在满足以下要求的前提下，求出 不同 骰子序列的数目：
 * 1、序列中任意 相邻 数字的 最大公约数 为 1 。
 * 2、序列中 相等 的值之间，至少有 2 个其他值的数字。正式地，如果第 i 次掷骰子的值 等于 第 j 次的值，那么 abs(i - j) > 2 。
 * 请你返回不同序列的 总数目 。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。
 * 如果两个序列中至少有一个元素不同，那么它们被视为不同的序列。
 * 提示：1 <= n <= 10^4
 * 链接：https://leetcode.cn/problems/number-of-distinct-roll-sequences
 */
public class Q2318 {

    public static void main(String[] args) {
        // 184
        System.out.println(new Q2318().distinctSequences(4));
        // 22
        System.out.println(new Q2318().distinctSequences(2));
    }

    public int distinctSequences(int n) {
        if (n == 1) return 6;
        int MOD = 1_000_000_007;
        long[][][] dp = new long[n][6][6];
        for (int i = 0; i < 6; i++)
            dp[0][i][0] = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 6; j++) { // end
                for (int k = 0; k < 6; k++) { // from
                    if (j != k && gcd(j + 1, k + 1) == 1) {
                        for (int l = 0; l < 6; l++) {
                            if (i < 2 || l != j) dp[i][j][k] = (dp[i][j][k] + dp[i - 1][k][l]) % MOD;
                        }
                    }
                }
            }
        }
        long ret = 0;
        for (int i = 0; i < 6; i++)
            for (int j = 0; j < 6; j++)
                ret = (ret + dp[n - 1][i][j]) % MOD;
        return (int) ret;
    }

    // 最大公约数
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
