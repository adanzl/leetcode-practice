package com.leo.leetcode.algorithm.q1300;

import java.util.Arrays;

public class Q1371 {
    public static void main(String[] args) {
        System.out.println(new Q1371().findTheLongestSubstring("eleetminicoworoep")); // 13
        System.out.println(new Q1371().findTheLongestSubstring("leetcodeisgreat")); // 5
        System.out.println(new Q1371().findTheLongestSubstring("bcbcbc")); // 6
    }

    public int findTheLongestSubstring(String s) {
        int[] mark = new int[32];
        Arrays.fill(mark, Integer.MIN_VALUE);
        mark[0] = -1;
        int index = 0, out = 0, len = 0;
        char[] str = s.toCharArray();
        for (int i = 0; i < str.length; i++) {
            int m = getMask(str[i]);
            if (m == -1) {
                len++;
            } else {
                index ^= m;
                if (mark[index] == Integer.MIN_VALUE)
                    mark[index] = i;
                len = i - mark[index];
            }
            out = Math.max(out, len);
        }
        return out;
    }

    int getMask(char c) {
        switch (c) {
            case 'a':
                return 1;
            case 'e':
                return 1 << 1;
            case 'i':
                return 1 << 2;
            case 'o':
                return 1 << 3;
            case 'u':
                return 1 << 4;
        }
        return -1;
    }
}