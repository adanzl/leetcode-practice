package com.leo.leetcode.algorithm.q0300;

/**
 * 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
 * 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
 * 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
 * （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
 * 后续挑战 :
 * 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
 * 的子序列。在这种情况下，你会怎样改变代码？
 * 链接：https://leetcode-cn.com/problems/is-subsequence
 */
class Q392 {

    public static void main(String[] args) {
        System.out.println(new Q392().isSubsequence("abc", "ahbgdc")); // true
        System.out.println(new Q392().isSubsequence("axc", "ahbgdc")); // false
        System.out.println(new Q392().isSubsequence("acb", "ahbgdc")); // false
        System.out.println(new Q392().isSubsequence("", "")); // true
    }

    public boolean isSubsequence(String s, String t) {
        if (s.length() == 0) return true;
        int i1 = 0, i2 = 0;
        char c = s.charAt(i1);
        while (i2 < t.length()) {
            if (c == t.charAt(i2)) {
                if (++i1 >= s.length()) break;
                c = s.charAt(i1);
            }
            i2++;
        }
        return i1 == s.length();
    }
}
