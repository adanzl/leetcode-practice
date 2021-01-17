package com.leo.leetcode.algorithm.q0000;

import java.util.Arrays;
import java.util.HashMap;

public class Q3 {

    public static void main(String[] args) {
        System.out.println(new Q3().lengthOfLongestSubstring1("abcabcbb")); // 3
        System.out.println(new Q3().lengthOfLongestSubstring1("pwwkew")); // 3
        System.out.println(new Q3().lengthOfLongestSubstring1("bbbbb")); // 1
        System.out.println(new Q3().lengthOfLongestSubstring1("tmmzuxt")); // 5
    }

    public int lengthOfLongestSubstring(String s) {
        int len = s.length();
        if (len == 0) return 0;
        int[] arr = new int[len];
        arr[0] = 1;
        HashMap<Character, Integer> tmp = new HashMap<>();
        tmp.put(s.charAt(0), 0);
        int ret = 1;
        for (int i = 1; i < len; i++) {
            char c = s.charAt(i);
            if (tmp.containsKey(c)) {
                int dIndex = tmp.get(c);
                arr[i] = i - dIndex;
                tmp.clear();
                for (int j = dIndex; j <= i; j++) {
                    tmp.put(s.charAt(j), j);
                }
            } else {
                int v = arr[i - 1] + 1;
                arr[i] = v;
                ret = Math.max(ret, v);
                tmp.put(c, i);
            }
        }
        return ret;
    }

    public int lengthOfLongestSubstring1(String s) {
        char[] str = s.toCharArray();
        if (str.length == 0) return 0;
        int[] charPos = new int[128];
        Arrays.fill(charPos, -1);
        int out = 0, len = 0, start = 0;
        for (int i = 0; i < str.length; i++) {
            int index = str[i];
            if (charPos[index] < start) {
                charPos[index] = i;
                len++;
                out = Math.max(out, len);
            } else {
                len = i - charPos[index];
                start = charPos[index] + 1;
                charPos[index] = i;
            }
        }
        return out;
    }
}
