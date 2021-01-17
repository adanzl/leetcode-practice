package com.leo.leetcode.algorithm.q0000;

/**
 * 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
 * '?' 可以匹配任何单个字符。
 * '*' 可以匹配任意字符串（包括空字符串）。
 * 两个字符串完全匹配才算匹配成功。
 * 说明:
 * s 可能为空，且只包含从 a-z 的小写字母。
 * p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
 * 链接：https://leetcode-cn.com/problems/wildcard-matching
 */
public class Q44 {
    public static void main(String[] args) {
        System.out.println(new Q44().isMatch("aa", "a")); // false
        System.out.println(new Q44().isMatch("aa", "*")); // true
        System.out.println(new Q44().isMatch("cb", "?a")); // false
        System.out.println(new Q44().isMatch("abcdeb", "*a*b")); // true
        System.out.println(new Q44().isMatch("acdcb", "a*c?b")); // false
    }

    public boolean isMatch(String s, String p) {
        int n = s.length(), m = p.length();
        s = " " + s;
        p = " " + p;
        int[][] dp = new int[n + 1][];
        for (int i = 0; i < n + 1; i++) dp[i] = new int[m + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= m; i++) {
            if (p.charAt(i) == '*') dp[0][i] = dp[0][i - 1];
        }
        for (int j = 1; j <= m; j++) {
            for (int i = 1; i <= n; i++) {
                if (p.charAt(j) != '*')
                    dp[i][j] = dp[i - 1][j - 1] == 1 && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?') ? 1 : 0;
                else dp[i][j] = dp[i - 1][j] | dp[i][j - 1];
            }
        }
        return dp[n][m] == 1;
    }
}
