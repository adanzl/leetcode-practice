package com.leo.leetcode.algorithm.q0300;

/**
 * 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
 * <p>
 * 链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
 */

public class Q395 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q395().longestSubstring("bbaaacbd", 3));
        // 0
        System.out.println(new Q395().longestSubstring("ababacb", 3));
        // 6
        System.out.println(new Q395().longestSubstring("caaabb", 0));
        // 3
        System.out.println(new Q395().longestSubstring("caaabb", 3));
        // 3
        System.out.println(new Q395().longestSubstring("aaabb", 3));
        // 5
        System.out.println(new Q395().longestSubstring("ababbc", 2));
    }

    public int longestSubstring(String s, int k) {
        return lSubString(s, k, 0, s.length());
    }

    int lSubString(String str, int k, int s, int e) {
        if (e - s < k) return 0;
        int ret = -1, pre = s;
        int[] sum = new int[26];
        for (int i = s; i < e; i++) ++sum[str.charAt(i) - 'a'];
        for (int i = s; i < e; i++) {
            if (sum[str.charAt(i) - 'a'] < k) {
                int len = lSubString(str, k, pre, i);
                ret = Math.max(ret, len);
                pre = i + 1;
            }
        }
        if (pre != s) ret = Math.max(ret, lSubString(str, k, pre, e));
        else ret = e-s;
        return ret;
    }
}
