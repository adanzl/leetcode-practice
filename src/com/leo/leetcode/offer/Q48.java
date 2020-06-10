package com.leo.leetcode.offer;

import java.util.Arrays;

public class Q48 {

    public static void main(String[] args) {
        new Q48().TestOJ();
    }

    public void TestOJ() {
        System.out.println(lengthOfLongestSubstring("abba")); // 2
        System.out.println(lengthOfLongestSubstring("abcabcbb")); // 3
    }

    public int lengthOfLongestSubstring(String s) {
        char[] str = s.toCharArray();
        if (str.length == 0) return 0;
        int[] mark = new int[str.length];
        int[] charPos = new int[128];
        Arrays.fill(mark, 1);
        Arrays.fill(charPos, -1);
        mark[0] = 1;
        charPos[str[0]] = 0;
        int out = 1;
        for (int i = 1; i < str.length; i++) {
            char c = str[i];
            if (charPos[c] == -1 || i - 1 - mark[i - 1] > charPos[c]) {
                mark[i] = mark[i - 1] + 1;
            } else {
                mark[i] = i - charPos[c];
            }
            charPos[c] = i;
            out = Math.max(out, mark[i]);
        }

        return out;
    }
}
