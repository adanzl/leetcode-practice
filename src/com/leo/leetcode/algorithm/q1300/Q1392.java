package com.leo.leetcode.algorithm.q1300;

/**
 * 「快乐前缀」是在原字符串中既是 非空 前缀也是后缀（不包括原字符串自身）的字符串。
 * 给你一个字符串 s，请你返回它的 最长快乐前缀。
 * 如果不存在满足题意的前缀，则返回一个空字符串。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只含有小写英文字母
 * 链接：https://leetcode-cn.com/problems/longest-happy-prefix
 */
public class Q1392 {

    public static void main(String[] args) {
        // ""
        System.out.println(new Q1392().longestPrefix("ababac"));
        // l
        System.out.println(new Q1392().longestPrefix("level"));
        // abab
        System.out.println(new Q1392().longestPrefix("ababab"));
        // leet
        System.out.println(new Q1392().longestPrefix("leetcodeleet"));
        // ""
        System.out.println(new Q1392().longestPrefix("a"));
    }

    public String longestPrefix(String s) {
        int len = s.length();
        int[] flags = new int[len + 1];
        for (int i = 1, k = 0; i < len; i++) {
            while (k > 0 && s.charAt(k) != s.charAt(i)) k = flags[k - 1];
            if (s.charAt(k) == s.charAt(i)) k++;
            flags[i] = k;
        }
        return s.substring(0, flags[len - 1]);
    }
}
