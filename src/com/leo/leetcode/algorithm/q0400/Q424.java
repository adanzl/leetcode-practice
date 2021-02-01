package com.leo.leetcode.algorithm.q0400;

/**
 * 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。
 * 在执行上述操作后，找到包含重复字母的最长子串的长度。
 * <p>
 * 注意：字符串长度 和 k 不会超过 10^4。
 * <p>
 * 链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
 */
public class Q424 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q424().characterReplacement("ABABCB", 2));
        // 6
        System.out.println(new Q424().characterReplacement("AABCABBB", 2));
        // 4
        System.out.println(new Q424().characterReplacement("AABABBA", 1));
        // 4
        System.out.println(new Q424().characterReplacement("ABAB", 2));
    }

    public int characterReplacement(String s, int k) {
        int ret = 0, l = 0, r = 0, nMain = 0;
        int[] marks = new int[26];
        char[] str = s.toCharArray();
        while (r < str.length) {
            int c = str[r] - 'A';
            marks[c]++;
            nMain = Math.max(nMain, marks[c]);
            // 此处使用while的优化，是由于最长子串更换目标之后，长度冗余增加很多，使用while一次削减多个长度
            while (r - l + 1 - nMain > k) {
                --marks[str[l] - 'A'];
                l++;
            }
            ret = Math.max(ret, r - l + 1);
            r++;
        }
        return ret;
    }
}
