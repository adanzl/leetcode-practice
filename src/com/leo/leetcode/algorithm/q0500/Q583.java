package com.leo.leetcode.algorithm.q0500;

/**
 * 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
 * 每步 可以删除任意一个字符串中的一个字符。
 * 提示：
 * 1、1 <= word1.length, word2.length <= 500
 * 2、word1 和 word2 只包含小写英文字母
 * 链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings/
 */
public class Q583 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q583().minDistance("sea", "eat"));
        // 4
        System.out.println(new Q583().minDistance("leetcode", "etco"));
    }

    public int minDistance(String word1, String word2) {
        int len1 = word1.length(), len2 = word2.length();
        int[][] dp = new int[len1 + 1][len2 + 1];
        for (int i = 0; i <= len1; i++) dp[i][0] = i;
        for (int i = 0; i <= len2; i++) dp[0][i] = i;
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];
                else dp[i][j] = Math.min(dp[i - 1][j] + 1, dp[i][j - 1] + 1);
            }
        }
        return dp[len1][len2];
    }
}
