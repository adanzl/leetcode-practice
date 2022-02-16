package com.leo.leetcode.algorithm.q0300;

/**
 * 给定两个字符串 s 和 t ，它们只包含小写字母。
 * 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
 * 请找出在 t 中被添加的字母。
 * 提示：
 * 1、0 <= s.length <= 1000
 * 2、t.length == s.length + 1
 * 3、s 和 t 只包含小写字母
 * 链接：https://leetcode-cn.com/problems/find-the-difference/
 */
public class Q389 {
    public static void main(String[] args) {
        // e
        System.out.println(new Q389().findTheDifference("abcd", "abcde"));
        // y
        System.out.println(new Q389().findTheDifference("", "y"));
    }

    public char findTheDifference(String s, String t) {
        char ret = ' ';
        int[] c = new int[26];
        for (int i = 0; i < s.length(); i++) c[s.charAt(i) - 'a']++;
        for (int i = 0; i < t.length(); i++) {
            if (c[t.charAt(i) - 'a']-- == 0) {
                ret = t.charAt(i);
                break;
            }
        }
        return ret;
    }
}
