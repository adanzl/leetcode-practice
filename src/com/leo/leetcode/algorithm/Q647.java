package com.leo.leetcode.algorithm;

import org.junit.Test;

public class Q647 {
    @Test
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
        int len = s.length() * 2 - 1, out = 0;
        for (int i = 0; i < len; i++) {
            int ext = i % 2;
            out += extend(s, i - ext, i + ext);
        }
        return out;
    }

    int extend(String s, int l, int r) {
        if (l < 0 || r >= s.length() * 2 - 1) return 0;
        int ext = (l + 1) % 2; // 0: *, 1: n
        if (s.charAt(l / 2) == s.charAt(r / 2)) return extend(s, l - 2, r + 2) + ext;
        return 0;
    }
}
