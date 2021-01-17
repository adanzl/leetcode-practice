package com.leo.leetcode.algorithm.q0100;

/**
 * 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
 * <p>
 * 说明：本题中，我们将空字符串定义为有效的回文串。
 * 链接：https://leetcode-cn.com/problems/valid-palindrome
 */
public class Q125 {

    public static void main(String[] args) {
        System.out.println(new Q125().isPalindrome("A man, a plan, a canal: Panama")); // true
        System.out.println(new Q125().isPalindrome("0P")); // false
        System.out.println(new Q125().isPalindrome(",.")); // true
        System.out.println(new Q125().isPalindrome("race a car")); // false
        System.out.println(new Q125().isPalindrome("")); // true
    }

    public boolean isPalindrome(String s) {
        char[] str = s.toCharArray();
        int l = 0, r = str.length - 1;
        while (l < r) {
            while (l < r && fit(str[l])) l++;
            while (l < r && fit(str[r])) r--;
            if ((str[l] & 0xDF) != (str[r] & 0xDF)) return false;
            l++;
            r--;
        }
        return true;
    }

    boolean fit(char c) {
        return (c < '0' || c > '9') && (c < 'a' || c > 'z') && (c < 'A' || c > 'Z');
    }

}
