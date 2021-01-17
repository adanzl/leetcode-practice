package com.leo.leetcode.algorithm.q0000;

/**
 * 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
 * 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
 */
public class Q5 {

    public static void main(String[] args) {
        new Q5().TestOJ();
    }

    public void TestOJ() {
        System.out.println(longestPalindrome("babad")); // bab
        System.out.println(longestPalindrome("cbbd")); // bb
        System.out.println(longestPalindrome("a")); // a
        System.out.println(longestPalindrome("abcda")); // a
        System.out.println(longestPalindrome("")); //
    }

    public String longestPalindrome(String s) {
        if (s.length() == 0) return "";
        char[] str = s.toCharArray();
        boolean[][] bMap = new boolean[str.length][];
        int len = 0, l = 0, r = 0;
        for (int i = 0; i < str.length; i++) {
            bMap[i] = new boolean[str.length];
            for (int j = 0; j <= i; j++) {
                if (i == j) {
                    bMap[i][j] = true;
                    continue;
                }
                if ((i > 0 && bMap[i - 1][j + 1] && str[i] == str[j]) || (j == i - 1 && str[i] == str[j])) {
                    bMap[i][j] = true;
                    if (len < i - j) {
                        len = i - j;
                        l = j;
                        r = i;
                    }
                }
            }
        }
        return s.substring(l, r + 1);
    }

//    public String longestPalindrome(String s) {
//        if (s == null || s.length() < 1) return "";
//        int start = 0, end = 0;
//        for (int i = 0; i < s.length(); i++) {
//            int len1 = expandAroundCenter(s, i, i);
//            int len2 = expandAroundCenter(s, i, i + 1);
//            int len = Math.max(len1, len2);
//            if (len > end - start) {
//                start = i - (len - 1) / 2;
//                end = i + len / 2;
//            }
//        }
//        return s.substring(start, end + 1);
//    }
//
//    int expandAroundCenter(String s, int l, int r) {
//        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
//            l--;
//            r++;
//        }
//
//        return r - l - 1;
//    }

}
