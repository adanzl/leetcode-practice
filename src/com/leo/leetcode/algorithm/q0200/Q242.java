package com.leo.leetcode.algorithm.q0200;

/**
 * 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
 * 说明:
 * 你可以假设字符串只包含小写字母。
 * 进阶:
 * 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
 * <p>
 * 链接：https://leetcode-cn.com/problems/valid-anagram/
 */
public class Q242 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q242().isAnagram("anagram", "nagaram"));
        // false
        System.out.println(new Q242().isAnagram("rat", "car"));
    }

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        char[] chars = new char[26];
        for (int i = 0; i < s.length(); i++) ++chars[s.charAt(i) - 'a'];
        for (int i = 0; i < t.length(); i++) if (chars[t.charAt(i) - 'a']-- == 0) return false;
        return true;
    }
}
