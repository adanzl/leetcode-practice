package com.leo.leetcode.algorithm.q0500;

/**
 * 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
 * 换句话说，第一个字符串的排列之一是第二个字符串的子串。
 * <p>
 * 注意：
 * 1、输入的字符串只包含小写字母
 * 2、两个字符串的长度都在 [1, 10,000] 之间
 * <p>
 * 链接：https://leetcode-cn.com/problems/permutation-in-string/
 */
public class Q567 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q567().checkInclusion("ab", "eidboaoo"));
        // true
        System.out.println(new Q567().checkInclusion("a", "ab"));
        // true
        System.out.println(new Q567().checkInclusion("ab", "eidbaooo"));
    }

    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        int[] sign = new int[26], flag = new int[26];
        int l = 0, r = 0, fit = 0, len = s2.length();
        for (int i = 0; i < s1.length(); i++) {
            int c = s1.charAt(i) - 'a';
            if (sign[c] == 0) fit++;
            sign[c]++;
        }
        while (r < len) {
            int rc = s2.charAt(r) - 'a';
            flag[rc]++;
            if (sign[rc] == flag[rc]) fit--;
            if (r >= s1.length()) {
                int lc = s2.charAt(l) - 'a';
                if (sign[lc] != 0 && sign[lc] == flag[lc]) fit++;
                flag[lc]--;
                l++;
            }
            if (fit == 0) return true;
            r++;
        }
        return false;
    }
}
