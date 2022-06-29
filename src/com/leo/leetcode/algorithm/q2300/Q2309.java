package com.leo.leetcode.algorithm.q2300;

/**
 * 给你一个由英文字母组成的字符串 s ，请你找出并返回 s 中的 最好 英文字母。返回的字母必须为大写形式。如果不存在满足条件的字母，则返回一个空字符串。
 * 最好 英文字母的大写和小写形式必须 都 在 s 中出现。
 * 英文字母 b 比另一个英文字母 a 更好 的前提是：英文字母表中，b 在 a 之 后 出现。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s 由小写和大写英文字母组成
 * 链接：https://leetcode.cn/problems/greatest-english-letter-in-upper-and-lower-case
 */
public class Q2309 {

    public static void main(String[] args) {
        // "Z"
        System.out.println(new Q2309().greatestLetter("nzmguNAEtJHkQaWDVSKxRCUivXpGLBcsjeobYPFwTZqrhlyOIfdM"));
        // "E"
        System.out.println(new Q2309().greatestLetter("lEeTcOdE"));
        // "R"
        System.out.println(new Q2309().greatestLetter("arRAzFif"));
        // ""
        System.out.println(new Q2309().greatestLetter("AbCdEfGhIjK"));
    }

    public String greatestLetter(String s) {
        char[] str = s.toCharArray();
        char ret = ' ';
        int[][] cnt = new int[26][2];
        for (char c : str) {
            int idx = -1;
            if (c >= 'a' && c <= 'z') {
                cnt[c - 'a'][0]++;
                idx = c - 'a';
            } else if (c >= 'A' && c <= 'Z') {
                cnt[c - 'A'][1]++;
                idx = c - 'A';
            }
            if (cnt[idx][0] > 0 && cnt[idx][1] > 0) {
                if (idx + 'A' > ret) {
                    ret = (char) (idx + 'A');
                }
            }
        }
        return String.valueOf(ret).trim();
    }
}
