package com.leo.leetcode.algorithm.q2300;

/**
 * 给你一个由小写字母组成的字符串 s ，和一个整数 k 。如果满足下述条件，则可以将字符串 t 视作是 理想字符串 ：
 * 1、t 是字符串 s 的一个子序列。
 * 2、t 中每两个 相邻 字母在字母表中位次的绝对差值小于或等于 k 。
 * 返回 最长 理想字符串的长度。
 * 字符串的子序列同样是一个字符串，并且子序列还满足：可以经由其他字符串删除某些字符（也可以不删除）但不改变剩余字符的顺序得到。
 * 注意：字母表顺序不会循环。例如，'a' 和 'z' 在字母表中位次的绝对差值是 25 ，而不是 1 。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、0 <= k <= 25
 * 3、s 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/longest-ideal-subsequence
 */
public class Q2370 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q2370().longestIdealString("acfgbd", 2));
        // 4
        System.out.println(new Q2370().longestIdealString("abcd", 3));
    }

    public int longestIdealString(String s, int k) {
        int[] count = new int[26];
        int n = s.length(), ret = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            int v = 0;
            for (int j = Math.max(0, c - 'a' - k); j <= Math.min(25, c - 'a' + k); j++) {
                v = Math.max(v, count[j] + 1);
            }
            ret = Math.max(ret, v);
            count[c - 'a'] = v;
        }
        return ret;
    }
}
