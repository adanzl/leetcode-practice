package com.leo.leetcode.algorithm.q1100;

/**
 * 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
 * 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
 * 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
 * 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
 * 提示：
 * 1、1 <= text1.length, text2.length <= 1000
 * 2、text1 和 text2 仅由小写英文字符组成。
 * 链接：https://leetcode-cn.com/problems/longest-common-subsequence
 */
public class Q1143 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1143().longestCommonSubsequence("abcde", "ace"));
        // 3
        System.out.println(new Q1143().longestCommonSubsequence("abc", "abc"));
        // 0
        System.out.println(new Q1143().longestCommonSubsequence("abc", "def"));
    }

    public int longestCommonSubsequence(String text1, String text2) {
        int len1 = text1.length(), len2 = text2.length();
        int[][] dp = new int[len1 + 1][len2 + 1];
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[len1][len2];
    }
}
