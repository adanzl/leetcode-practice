package com.leo.leetcode.algorithm.q0400;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
 * 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
 * <p>
 * 说明：
 * 1、字母异位词指字母相同，但排列不同的字符串。
 * 2、不考虑答案输出的顺序。
 * <p>
 * 链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
 */
public class Q438 {

    public static void main(String[] args) {
        System.out.println(new Q438().findAnagrams("cbaebabac", "bac")); // [0, 6]
        System.out.println(new Q438().findAnagrams("abab", "ab")); // [0, 1, 2]
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
