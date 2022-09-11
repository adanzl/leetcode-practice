package com.leo.leetcode.algorithm.q2300;

/**
 * 如果一个整数 n 在 b 进制下（b 为 2 到 n - 2 之间的所有整数）对应的字符串 全部 都是 回文的 ，那么我们称这个数 n 是 严格回文 的。
 * 给你一个整数 n ，如果 n 是 严格回文 的，请返回 true ，否则返回 false 。
 * 如果一个字符串从前往后读和从后往前读完全相同，那么这个字符串是 回文的 。
 * 提示：4 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/strictly-palindromic-number
 */
public class Q2396 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q2396().isStrictlyPalindromic(9));
        // false
        System.out.println(new Q2396().isStrictlyPalindromic(4));
    }

    public boolean isStrictlyPalindromic(int n) {
        for (int i = 2; i <= n - 2; i++) {
            String nStr = getChar(n, i);
            int len = nStr.length();
            for (int j = 0; j < len / 2; j++) {
                if (nStr.charAt(j) != nStr.charAt(len - 1 - j)) return false;
            }
        }
        return true;
    }

    String getChar(int n, int b) {
        int num = n;
        StringBuilder ans = new StringBuilder();
        while (num != 0) {
            ans.append(num % b);
            num /= b;
        }
        return ans.toString();
    }
}