package com.leo.leetcode.algorithm.q2200;

/**
 * 字符串的 波动 定义为子字符串中出现次数 最多 的字符次数与出现次数 最少 的字符次数之差。
 * 给你一个字符串 s ，它只包含小写英文字母。请你返回 s 里所有 子字符串的 最大波动 值。
 * 子字符串 是一个字符串的一段连续字符序列。
 * 提示：
 * 1、1 <= s.length <= 10^4
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/substring-with-largest-variance
 */
public class Q2272 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q2272().largestVariance("bbc"));
        // 3
        System.out.println(new Q2272().largestVariance("icexiahccknibwuwgi"));
        // 0
        System.out.println(new Q2272().largestVariance("aaaaa"));
        // 3
        System.out.println(new Q2272().largestVariance("aababbb"));
        // 0
        System.out.println(new Q2272().largestVariance("abcde"));
    }

    // 枚举所有最大最小字母的组合
    public int largestVariance(String s) {
        int n = s.length(), ret = 0;
        for (int c1 = 'a'; c1 <= 'z'; c1++) {
            for (int c2 = 'a'; c2 <= 'z'; c2++) {
                if (c1 == c2) continue;
                int[] dp = new int[]{0, -100001};
                for (int i = 0; i < n; i++) {
                    if (s.charAt(i) == c1) {
                        dp[0]++;
                        dp[1]++;
                    } else if (s.charAt(i) == c2) {
                        dp[1] = Math.max(dp[1], dp[0]) - 1;
                        dp[0] = 0;
                    }
                    ret = Math.max(ret, dp[1]);
                }
            }
        }
        return ret;
    }
}
