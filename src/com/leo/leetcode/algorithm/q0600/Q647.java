package com.leo.leetcode.algorithm.q0600;

/**
 * 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
 * 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
 * 提示：
 *     输入的字符串长度不会超过 1000 。
 * 链接：https://leetcode-cn.com/problems/palindromic-substrings/
 */
public class Q647 {

    public static void main(String[] args) {
        new Q647().TestOJ();
    }

    public void TestOJ() {
        System.out.println(countSubstrings("aba")); // 4
        System.out.println(countSubstrings("")); // 0
        System.out.println(countSubstrings("abc")); // 3
        System.out.println(countSubstrings("abc1")); // 4
        System.out.println(countSubstrings("aaa")); // 6
    }

    // abc1 -> a*b*c*1, abc -> a*b*c,
    // 0123 || 0123456, 012 || 01234,
    public int countSubstrings(String s) {
        int len = (s.length() << 1) - 1, out = 0;
        for (int i = 0; i < len; i++) {
            int ext = i & 0x1;
            out += extend(s, i - ext, i + ext);
        }
        return out;
    }

    int extend(String s, int l, int r) {
        if (l < 0 || r >= (s.length() << 1) - 1) return 0;
        int ext = (l + 1) & 0x1; // 0: *, 1: n
        if (s.charAt(l >> 1) == s.charAt(r >> 1)) return extend(s, l - 2, r + 2) + ext;
        return 0;
    }
}
