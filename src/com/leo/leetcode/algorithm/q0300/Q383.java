package com.leo.leetcode.algorithm.q0300;

/**
 * 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
 * 如果可以，返回 true ；否则返回 false 。
 * magazine 中的每个字符只能在 ransomNote 中使用一次。
 * 提示：
 * 1、1 <= ransomNote.length, magazine.length <= 10^5
 * 2、ransomNote 和 magazine 由小写英文字母组成
 * 链接：https://leetcode-cn.com/problems/ransom-note
 */
public class Q383 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q383().canConstruct("a", "b"));
        // false
        System.out.println(new Q383().canConstruct("aa", "ab"));
        // true
        System.out.println(new Q383().canConstruct("aa", "aab"));
    }

    public boolean canConstruct(String ransomNote, String magazine) {
        int[] chars = new int[26];
        int count = 0;
        for (char c : ransomNote.toCharArray()) {
            int idx = c - 'a';
            if (chars[idx]++ == 0) count++;
        }
        for (char c : magazine.toCharArray()) {
            int idx = c - 'a';
            if (--chars[idx] == 0) count--;
        }
        return count == 0;
    }
}
