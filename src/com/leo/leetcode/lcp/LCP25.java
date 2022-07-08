package com.leo.leetcode.lcp;

/**
 * 小扣在秋日市集购买了一个古董键盘。由于古董键盘年久失修，键盘上只有 26 个字母 a~z 可以按下，且每个字母最多仅能被按 k 次。
 * 小扣随机按了 n 次按键，请返回小扣总共有可能按出多少种内容。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。
 * 提示：
 * 1、1 <= k <= 5
 * 2、1 <= n <= 26*k
 * 链接：https://leetcode.cn/problems/Uh984O
 */
public class LCP25 {

    public static void main(String[] args) {
        // 735365374
        System.out.println(new LCP25().keyboard(5, 130));
        // 26
        System.out.println(new LCP25().keyboard(1, 1));
        // 650
        System.out.println(new LCP25().keyboard(1, 2));
    }

    public int keyboard(int k, int n) {
        int MOD = 1_000_000_007;
        long[][] dp = new long[27][n + 1]; // dp[i][j] 使用i个字母，按键j次
        int[][] C = new int[k + 1][n + 2]; // 小-大 C[m][n]=C[m][n-1]+C[m-1][n-1] 组合数计算
        C[0][0] = 1;
        for (int i = 0; i <= k; i++) {
            for (int j = 1; j < n + 2; j++) {
                if (i == 0) C[i][j] = 1;
                else C[i][j] = C[i][j - 1] + C[i - 1][j - 1];
            }
        }
        dp[0][0] = 1;
        for (int i = 1; i < 27; i++) {
            dp[i][0] = 1;
            for (int j = 1; j <= n; j++) {
                for (int l = 0; l <= Math.min(k, j); l++) {
                    // 插空
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - l] * C[l][j]) % MOD;
                }
            }
        }
        return (int) dp[26][n];
    }
}
