package com.leo.leetcode.algorithm.q0500;

/**
 * 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
 * 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s 仅由小写英文字母组成
 * 链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
 */
public class Q516 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q516().longestPalindromeSubSeq("bbbab"));
        // 2
        System.out.println(new Q516().longestPalindromeSubSeq("cbbd"));
    }

    public int longestPalindromeSubSeq(String s) {
        int len = s.length();
        int[][] dp = new int[len][len];
        for (int i = 0; i < len; i++) dp[i][i] = 1;
        for (int i = len - 1; i >= 0; i--) {
            for (int j = i + 1; j < len; j++) {
                if (s.charAt(i) == s.charAt(j)) dp[i][j] = dp[i + 1][j - 1] + 2;
                else dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
        return dp[0][len - 1];
    }
}
