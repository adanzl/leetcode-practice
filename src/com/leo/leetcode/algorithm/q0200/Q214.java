package com.leo.leetcode.algorithm.q0200;

/**
 * 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。
 * 找到并返回可以用这种方式转换的最短回文串。
 * 链接：https://leetcode-cn.com/problems/shortest-palindrome/
 */
public class Q214 {

    public static void main(String[] args) {
        System.out.println(new Q214().shortestPalindrome("ba")); // "aba"
        System.out.println(new Q214().shortestPalindrome("aba")); // "aba"
        System.out.println(new Q214().shortestPalindrome("a")); // a
        System.out.println(new Q214().shortestPalindrome("abcd")); // dcbabcd
        System.out.println(new Q214().shortestPalindrome("aacecaaa")); // aaacecaaa
    }

    public String shortestPalindrome(String s) {
        if (s.length() == 0) return "";
        int index = s.length() >> 1, mainIndex = 0;
        char[] str = s.toCharArray();
        int loopLen = 1;
        while (index > 0) {
            loopLen = check(str, index);
            if (loopLen > 1) break;
            --index;
        }
        int ext = s.length() - loopLen;
        char[] out = new char[s.length() + ext];
        for (int i = 0; i < ext; i++)
            out[mainIndex++] = str[str.length - 1 - i];
        for (char c : str) out[mainIndex++] = c;
        return new String(out);
    }

    int check(char[] str, int offset) {
        int len = 0;
        for (int i = 1; i <= offset && offset + i < str.length; i++) {
            if (str[offset - i] != str[offset + i]) {
                break;
            }
            len = i;
        }
        if (len == offset) return (offset << 1) + 1;
        len = 0;
        for (int i = 1; i <= offset && offset + i < str.length; i++) {
            if (str[offset - i] != str[offset - 1 + i]) {
                break;
            }
            len = i;
        }
        return len == offset ? (offset << 1) : 1;
    }
}