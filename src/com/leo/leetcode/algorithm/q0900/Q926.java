package com.leo.leetcode.algorithm.q0900;

/**
 * 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。
 * 给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。
 * 返回使 s 单调递增的最小翻转次数。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 为 '0' 或 '1'
 * 链接：https://leetcode.cn/problems/flip-string-to-monotone-increasing
 */
public class Q926 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q926().minFlipsMonoIncr("00110"));
        // 2
        System.out.println(new Q926().minFlipsMonoIncr("010110"));
        // 2
        System.out.println(new Q926().minFlipsMonoIncr("00011000"));
    }

    public int minFlipsMonoIncr(String s) {
        int n = s.length();
        char[] str = s.toCharArray();
        int[] dp0 = new int[n + 1], dp1 = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int min = Math.min(dp1[i], dp0[i]);
            if (str[i] == '0') {
                dp0[i + 1] = dp0[i];
                dp1[i + 1] = min + 1;
            } else {
                dp0[i + 1] = dp0[i] + 1;
                dp1[i + 1] = min;
            }
        }
        return Math.min(dp0[n], dp1[n]);
    }
}
