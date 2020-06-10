package com.leo.leetcode.algorithm;

public class Q680 {

    public static void main(String[] args) {
        System.out.println(new Q680().validPalindrome("abc")); // false
    }

    public boolean validPalindrome(String s) {
        char[] str = s.toCharArray();
        int l = 0, r = str.length - 1;
        while (l <= r) {
            if (str[l] != str[r]) return isPalindrome(str, l + 1, r) || isPalindrome(str, l, r - 1);
            l++;
            r--;
        }

        return true;
    }

    boolean isPalindrome(char[] str, int s, int e) {
        int mid = (e - s) >> 1;
        for (int i = 0; i <= mid; i++) {
            if (str[s + i] != str[e - i]) return false;
        }
        return true;
    }
}
