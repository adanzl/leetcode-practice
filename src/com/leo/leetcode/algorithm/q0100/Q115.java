package com.leo.leetcode.algorithm.q0100;

/**
 * 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
 * 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
 * 题目数据保证答案符合 32 位带符号整数范围。
 * 链接：https://leetcode-cn.com/problems/distinct-subsequences
 */
public class Q115 {
    public static void main(String[] args) {
        System.out.println(new Q115().numDistinct("bbt", "bt")); // 2
        System.out.println(new Q115().numDistinct("bbtt", "btt")); // 2
        System.out.println(new Q115().numDistinct("babgbag", "bag")); // 5
        System.out.println(new Q115().numDistinct("rabbit", "rabbit")); // 1
        System.out.println(new Q115().numDistinct("ababgbag", "bcddceeeebecbc")); // 0
        System.out.println(new Q115().numDistinct("adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc"
                , "bcddceeeebecbc")); // 700531452
    }

    public int numDistinct(String s, String t) {
        int lenS = s.length(), lenT = t.length();
        if (lenS == 0 || lenT == 0 || lenS < lenT) return 0;
        int[][] marks = new int[lenS][lenT];
        for (int i = 0; i < marks.length; i++) {
            if (i == 0) marks[i][0] = s.charAt(0) == t.charAt(0) ? 1 : 0;
            else marks[i][0] = marks[i - 1][0] + (s.charAt(i) == t.charAt(0) ? 1 : 0);
        }
        for (int i = 1; i < lenS; i++) {
            for (int j = 1; j < lenT; j++) {
                marks[i][j] = s.charAt(i) == t.charAt(j) ? marks[i - 1][j - 1] + marks[i - 1][j] : marks[i - 1][j];
            }
        }
        return marks[lenS - 1][lenT - 1];
    }

    // 备忘录法
//    int numDist(char[] str1, int offset1, char[] str2, int offset2, int[][] marks) {
//        if (str2.length == offset2) return 1;
//        if (marks[offset1][offset2] != -1) return marks[offset1][offset2];
//        int out = 0;
//        for (int i = offset1; i <= str1.length - str2.length + offset2; i++) {
//            if (str1[i] == str2[offset2])
//                out += numDist(str1, i + 1, str2, offset2 + 1, marks);
//        }
//        marks[offset1][offset2] = out;
//        return out;
//    }
}
