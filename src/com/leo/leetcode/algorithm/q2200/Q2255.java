package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给你一个字符串数组 words 和一个字符串 s ，其中 words[i] 和 s 只包含 小写英文字母 。
 * 请你返回 words 中是字符串 s 前缀 的 字符串数目 。
 * 一个字符串的 前缀 是出现在字符串开头的子字符串。子字符串 是一个字符串中的连续一段字符序列。
 * 提示：
 * 1、1 <= words.length <= 1000
 * 2、1 <= words[i].length, s.length <= 10
 * 3、words[i] 和 s 只 包含小写英文字母。
 * 链接：https://leetcode-cn.com/problems/count-prefixes-of-a-given-string
 */
public class Q2255 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2255().countPrefixes(stringToStringArray(" [\"a\",\"b\",\"c\",\"ab\",\"bc\",\"abc\"]"), "abc"));
        // 2
        System.out.println(new Q2255().countPrefixes(stringToStringArray("[\"a\",\"a\"]"), "aa"));
    }

    public int countPrefixes(String[] words, String s) {
        int ret = 0;
        for (String word : words) if (s.startsWith(word)) ret++;
        return ret;
    }
}
