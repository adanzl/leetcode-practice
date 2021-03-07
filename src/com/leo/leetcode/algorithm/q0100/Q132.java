package com.leo.leetcode.algorithm.q0100;

/**
 * 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
 * 返回符合要求的 最少分割次数 。
 * <p>
 * 提示：
 * 1、1 <= s.length <= 2000
 * 2、s 仅由小写英文字母组成
 * <p>
 * 链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii/
 */
public class Q132 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q132().minCut("abcccb"));
        // 1
        System.out.println(new Q132().minCut("abbab"));
        // 0
        System.out.println(new Q132().minCut("efe"));
        // 1
        System.out.println(new Q132().minCut("aab"));
        // 0
        System.out.println(new Q132().minCut("a"));
        // 1
        System.out.println(new Q132().minCut("ab"));
    }

    public int minCut(String s) {
        int len = s.length();
        // 上三角
        boolean[][] marks = new boolean[s.length()][s.length()];
        char[] str = s.toCharArray();
        int[] dp = new int[len + 1];
        for (int i = 0; i < len; i++) marks[i][i] = true;
        for (int i = 0; i < len - 1; i++) {
            // odd
            for (int j = 1; j + i < len && i >= j; j++) {
                if (str[i - j] == str[i + j]) marks[i - j][i + j] = true;
                else break;
            }
            // even
            if (str[i] != str[i + 1]) continue;
            marks[i][i + 1] = true;
            for (int j = 2; j + i < len && i >= j - 1; j++) {
                if (str[i - j + 1] == str[i + j]) marks[i - j + 1][i + j] = true;
                else break;
            }
        }
        dp[0] = 0;
        for (int i = 0; i < len; i++) {
            dp[i + 1] = 0;
            int c = dp[i] + 1;
            for (int j = i - 1; j >= 0; j--)
                if (marks[j][i]) c = Math.min(c, dp[j] + 1);
            dp[i + 1] = c;
        }
        return dp[len] - 1;
    }
}
