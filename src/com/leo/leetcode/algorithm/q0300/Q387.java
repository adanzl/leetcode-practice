package com.leo.leetcode.algorithm.q0300;

/**
 * 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
 * 提示：你可以假定该字符串只包含小写字母。
 * <p>
 * 链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string/
 */
public class Q387 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q387().firstUniChar("leetcode"));
        // 2
        System.out.println(new Q387().firstUniChar("loveleetcode"));
    }

    public int firstUniChar(String s) {
        int[] flags = new int[26];
        for (int i = 0; i < s.length(); i++) ++flags[s.charAt(i) - 'a'];
        for (int i = 0; i < s.length(); i++) if (flags[s.charAt(i) - 'a'] == 1) return i;
        return -1;
    }
}
