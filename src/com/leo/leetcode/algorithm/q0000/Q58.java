package com.leo.leetcode.algorithm.q0000;

public class Q58 {

    public static void main(String[] args) {
        new Q58().TestOJ();
    }

    public void TestOJ() {
        System.out.println(lengthOfLastWord("b   a    ")); // 1
        System.out.println(lengthOfLastWord("Hello World")); // 5
        System.out.println(lengthOfLastWord("Hello")); // 5
    }

    public int lengthOfLastWord(String s) {
        String str = s.trim();
        if (str.length() == 0) return 0;
        return str.length() - str.lastIndexOf(' ') - 1;
    }
}
