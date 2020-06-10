package com.leo.leetcode.algorithm;

import org.junit.Test;

public class Q394 {
    @Test
    public void TestOJ() {
        System.out.println(decodeString("3[a]a2[bc]")); // "aaaabcbc"
        System.out.println(decodeString("3[a2[c]]")); // "accaccacc"
        System.out.println(decodeString("2[abc]3[cd]ef")); // "abcabccdcdcdef"
        System.out.println(decodeString("3[a]2[bc]")); // "aaabcbc"
    }

    private int index;

    public String decodeString(String s) {
        index = 0;
        StringBuilder sb = new StringBuilder();
        while (index < s.length()) {
            sb.append(decode(s));
        }
        return sb.toString();
    }

    private StringBuilder decode(String s) {
        StringBuilder content = new StringBuilder();
        int k;
        if (isNum(s.charAt(index))) {
            int i = 0;
            while (s.charAt(index + i) != '[') i++;
            k = Integer.parseInt(s.substring(index, index + i));
            index += i + 1;

            while (s.charAt(index) != ']') {
                if (isNum(s.charAt(index))) {
                    content.append(decode(s));
                } else {
                    content.append(s.charAt(index));
                    index++;
                }
            }
            index++;
        } else {
            k = 1;
            while (index < s.length() && !isNum(s.charAt(index))) {
                content.append(s.charAt(index));
                index++;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
            sb.append(content);
        }
        return sb;
    }

    private boolean isNum(char c) {
        return c >= '0' && c <= '9';
    }
}
