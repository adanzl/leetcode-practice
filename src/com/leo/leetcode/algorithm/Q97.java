package com.leo.leetcode.algorithm;

/**
 * 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
 * 链接：https://leetcode-cn.com/problems/interleaving-string/
 */
public class Q97 {
    public static void main(String[] args) {
        System.out.println(new Q97().isInterleave("aabcc", "dbbca", "aadbbcbcac")); // true
        System.out.println(new Q97().isInterleave("aabcc", "dbbca", "aadbbbaccc")); // false
        System.out.println(new Q97().isInterleave("", "", "")); // true
        System.out.println(new Q97().isInterleave("a", "", "a")); // true
    }

    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) return false;
        boolean[][][] dp = new boolean[s3.length() + 1][s1.length() + 1][s2.length() + 1]; // s2, s3, s1
        for (int i = 0; i <= s1.length(); i++) for (int j = 0; j <= s2.length(); j++) dp[0][i][j] = false;
        dp[0][0][0] = true;
        for (int i = 1; i <= s3.length(); i++) {
            char c = s3.charAt(i - 1);
            for (int i1 = 0; i1 <= s1.length() && i1 <= i; i1++) {
                int i2 = i - i1;
                if (i2 > s2.length()) continue;
                if (i1 == 0) dp[i][i1][i2] = dp[i - 1][i1][i2 - 1] && s2.charAt(i2 - 1) == c;
                else if (i2 == 0) dp[i][i1][i2] = dp[i - 1][i1 - 1][i2] && s1.charAt(i1 - 1) == c;
                else {
                    dp[i][i1][i2] = (s1.charAt(i1 - 1) == c && dp[i - 1][i1 - 1][i2])
                            || (s2.charAt(i2 - 1) == c && dp[i - 1][i1][i2 - 1]);
                }
            }
        }
        return dp[s3.length()][s1.length()][s2.length()];

    }
}
