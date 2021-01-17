package com.leo.leetcode.algorithm.q0000;

public class Q9 {

    public static void main(String[] args) {
        System.out.println(new Q9().isPalindrome(121)); // true
        System.out.println(new Q9().isPalindrome(-121)); // false
        System.out.println(new Q9().isPalindrome(0)); // true
    }

    public boolean isPalindrome(int x) {
        char[] num = Integer.toString(x).toCharArray();
        for (int i = 0; i < num.length >> 1; i++) {
            if (num[i] != num[num.length - 1 - i]) return false;
        }
        return true;
    }
}
