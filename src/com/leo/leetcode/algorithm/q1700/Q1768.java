package com.leo.leetcode.algorithm.q1700;

/**
 * 给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
 * 返回 合并后的字符串 。
 * 提示：
 * 1、1 <= word1.length, word2.length <= 100
 * 2、word1 和 word2 由小写英文字母组成
 * 链接：https://leetcode-cn.com/problems/merge-strings-alternately
 */
public class Q1768 {

    public static void main(String[] args) {
        // "apbqcr"
        System.out.println(new Q1768().mergeAlternately("abc", "pqr"));
        // "apbqrs"
        System.out.println(new Q1768().mergeAlternately("ab", "pqrs"));
        // "apbqcd"
        System.out.println(new Q1768().mergeAlternately("abcd", "pq"));
        // "abcd"
        System.out.println(new Q1768().mergeAlternately("abcd", ""));
    }

    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int len1 = word1.length(), len2 = word2.length(), i = 0;
        for (; i < len1 && i < len2; i++) {
            sb.append(word1.charAt(i)).append(word2.charAt(i));
        }
        if (i < len1) sb.append(word1.substring(i));
        if (i < len2) sb.append(word2.substring(i));
        return sb.toString();
    }
}
