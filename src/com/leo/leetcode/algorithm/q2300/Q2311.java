package com.leo.leetcode.algorithm.q2300;

/**
 * 给你一个二进制字符串 s 和一个正整数 k 。
 * 请你返回 s 的 最长 子序列，且该子序列对应的 二进制 数字小于等于 k 。
 * 注意：
 * 1、子序列可以有 前导 0 。
 * 2、空字符串视为 0 。
 * 3、子序列 是指从一个字符串中删除零个或者多个字符后，不改变顺序得到的剩余字符序列。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s[i] 要么是 '0' ，要么是 '1' 。
 * 3、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/longest-binary-subsequence-less-than-or-equal-to-k
 */
public class Q2311 {

    public static void main(String[] args) {
        // 96
        System.out.println(new Q2311().longestSubsequence("111100010000011101001110001111000000001011101111111110111000011111011000010101110100110110001111001001011001010011010000011111101001101000000101101001110110000111101011000101"
                , 11713332));
        // 6
        System.out.println(new Q2311().longestSubsequence("00101001", 1));
        // 5
        System.out.println(new Q2311().longestSubsequence("1001010", 5));
        // 7
        System.out.println(new Q2311().longestSubsequence("0111101", 518459120));
    }

    public int longestSubsequence(String s, int k) {
        char[] str = s.toCharArray();
        int n = s.length(), ret = 0;
        long num = 0;
        boolean flag = true;
        for (int i = n - 1; i >= 0; i--) {
            if (str[i] == '0') ret++;
            else {
                long v = (1L << (n - i - 1)) + num;
                if (v <= k && flag) {
                    num = v;
                    ret++;
                } else {
                    flag = false;
                }
            }
        }
        return ret;
    }
}
