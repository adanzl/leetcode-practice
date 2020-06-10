package com.leo.leetcode.offer;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Q38 {

    public static void main(String[] args) {
        new Q38().TestOJ();
    }
    public void TestOJ() {
        System.out.println(Arrays.toString(permutation("abc")));
        System.out.println(Arrays.toString(permutation("ab")));
    }

    public String[] permutation(String s) {
        char[] str = s.toCharArray();
        Set<String> out = new HashSet<>();
        per(str, 0, str.length, out);
        return out.toArray(new String[0]);
    }

    void per(char[] str, int start, int end, Set<String> out) {
        if (end - start <= 1) {
            out.add(new String(str));
            return;
        }
        for (int i = start; i < end; i++) {
            swap(str, start, i);
            per(str, start + 1, end, out);
            swap(str, start, i);
        }
    }

    void swap(char[] str, int l, int r) {
        char c = str[l];
        str[l] = str[r];
        str[r] = c;
    }
}
