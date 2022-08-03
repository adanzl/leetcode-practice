package com.leo.leetcode.algorithm.q0700;

/**
 * 给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。
 * 提示:
 * 1、0 <= s1.length, s2.length <= 1000
 * 2、s1 和 s2 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/
 */
public class Q712 {

    public static void main(String[] args) {
        // 231
        System.out.println(new Q712().minimumDeleteSum("sea", "eat"));
        // 403
        System.out.println(new Q712().minimumDeleteSum("delete", "leet"));
    }

    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) dp[i][0] = dp[i - 1][0] + s1.charAt(i - 1);
        for (int i = 1; i <= n; i++) dp[0][i] = dp[0][i - 1] + s2.charAt(i - 1);
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                char c1 = s1.charAt(i - 1), c2 = s2.charAt(j - 1);
                if (c1 == c2) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = dp[i - 1][j - 1] + c1 + c2;
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + c1);
                    dp[i][j] = Math.min(dp[i][j], dp[i][j - 1] + c2);
                }
            }
        }
        return dp[m][n];
    }
}
