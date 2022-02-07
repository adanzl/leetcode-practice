package com.leo.leetcode.algorithm.q0000;

/**
 * 一条包含字母 A-Z 的消息通过以下方式进行了编码：
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * 给定一个只包含数字的非空字符串，请计算解码方法的总数。
 * 链接：https://leetcode-cn.com/problems/decode-ways
 */
public class Q91 {
    public static void main(String[] args) {
        System.out.println(new Q91().numDecoding("10")); // 1
        System.out.println(new Q91().numDecoding("101")); // 1
        System.out.println(new Q91().numDecoding("100")); // 0
        System.out.println(new Q91().numDecoding("17")); // 2
        System.out.println(new Q91().numDecoding("0")); // 0
        System.out.println(new Q91().numDecoding("226")); // 3
    }

    public int numDecoding(String s) {
        char[] str = s.toCharArray();
        int[] marks = new int[str.length];
        marks[0] = str[0] > '0' ? 1 : 0;
        if (marks.length > 1) marks[1] = (check(str[0], str[1]) ? 1 : 0) + (str[1] > '0' ? marks[0] : 0);
        for (int i = 2; i < marks.length; i++) {
            boolean flag = check(str[i - 1], str[i]);
            marks[i] = (str[i] > '0' ? marks[i - 1] : 0) + (flag ? marks[i - 2] : 0);
        }
        return marks[marks.length - 1];
    }

    boolean check(char c1, char c2) {
        return c1 == '1' || (c1 == '2' && c2 <= '6');
    }
}
