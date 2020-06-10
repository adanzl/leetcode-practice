package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q438 {
    public void TestOJ() {
        System.out.println(findAnagrams("cbaebabac", "bac")); // [0, 6]
        System.out.println(findAnagrams("abab", "ab")); // [0, 1, 2]
    }

    public List<Integer> findAnagrams(String s, String p) {
        char[] pArr = p.toCharArray(), src = s.toCharArray();
        Arrays.sort(pArr);
        List<Integer> out = new ArrayList<>();
        int lastFind = 0;
        for (int i = 0; i < s.length() - p.length() + 1; i++) {
            if (lastFind != 0) {
                if (src[i - lastFind] == src[i + p.length() - 1]) {
                    out.add(i);
                    lastFind = 1;
                    continue;
                } else {
                    lastFind = 0;
                }
            }
            if (compare(src, i, i + p.length(), pArr)) {
                out.add(i);
                lastFind = 1;
            }
        }
        return out;
    }

    private boolean compare(char[] src, int l, int r, char[] arr) {
        int[] m = new int[256];
        int[] n = new int[256];
        for (int i = l; i < r; i++) {
            m[src[i]] += 1;
        }
        for (char c : arr) {
            n[c] += 1;
        }
        for (int i = 0; i < m.length; i++) {
            if (m[i] != n[i])
                return false;
        }
        return true;
    }

}
