package com.leo.leetcode.algorithm.q0500;

/**
 * 给你两个字符串 a 和 b，请返回 这两个字符串中 最长的特殊序列  。如果不存在，则返回 -1 。
 * 「最长特殊序列」 定义如下：该序列为 某字符串独有的最长子序列（即不能是其他字符串的子序列） 。
 * 字符串 s 的子序列是在从 s 中删除任意数量的字符后可以获得的字符串。
 * 例如，“abc” 是 “aebdc” 的子序列，因为您可以删除 “aebdc” 中的下划线字符来得到 “abc” 。
 * “aebdc” 的子序列还包括 “aebdc” 、 “aeb” 和 “” (空字符串)。
 * 提示：
 * 1、1 <= a.length, b.length <= 100
 * 2、a 和 b 由小写英文字母组成
 * 链接：https://leetcode-cn.com/problems/longest-uncommon-subsequence-i
 */
public class Q521 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q521().findLUSLength("a", "aaa"));
        // -1
        System.out.println(new Q521().findLUSLength("aweffwaf", "aweffwaf"));
        // 17
        System.out.println(new Q521().findLUSLength("aefawfawfawfaw", "aefawfeawfwafwaef"));
        // 3
        System.out.println(new Q521().findLUSLength("aba", "cdc"));
        // 3
        System.out.println(new Q521().findLUSLength("aaa", "bbb"));
        // -1
        System.out.println(new Q521().findLUSLength("aaa", "aaa"));
    }

    public int findLUSLength(String a, String b) {
        if (a.length() != b.length()) return Math.max(a.length(), b.length());
        int[][] dp = new int[a.length() + 1][b.length() + 1];
        for (int i = 1; i <= a.length(); i++) {
            for (int j = 1; j <= b.length(); j++) {
                if (a.charAt(i - 1) == b.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];
                else dp[i][j] = Math.max(i, j);
            }
        }
        int ret = dp[a.length()][b.length()];
        return ret == 0 ? -1 : ret;
    }
}
