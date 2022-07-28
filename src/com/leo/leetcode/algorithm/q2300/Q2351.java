package com.leo.leetcode.algorithm.q2300;

/**
 * 给你一个由小写英文字母组成的字符串 s ，请你找出并返回第一个出现 两次 的字母。
 * 注意：
 * 1、如果 a 的 第二次 出现比 b 的 第二次 出现在字符串中的位置更靠前，则认为字母 a 在字母 b 之前出现两次。
 * 2、s 包含至少一个出现两次的字母。
 * 提示：
 * 1、2 <= s.length <= 100
 * 2、s 由小写英文字母组成
 * 3、s 包含至少一个重复字母
 * 链接：https://leetcode.cn/problems/first-letter-to-appear-twice
 */
public class Q2351 {

    public static void main(String[] args) {
        // c
        System.out.println(new Q2351().repeatedCharacter("abccbaacz"));
        // d
        System.out.println(new Q2351().repeatedCharacter("abcdd"));
    }

    public char repeatedCharacter(String s) {
        char[] str = s.toCharArray();
        int[] count = new int[26];
        for (char c : str) {
            count[c - 'a']++;
            if (count[c - 'a'] == 2) return c;
        }
        return ' ';
    }
}
