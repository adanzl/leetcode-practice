package com.leo.leetcode.algorithm.q1600;

/**
 * 请你设计一个可以解释字符串 command 的 Goal 解析器 。command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成。
 * Goal 解析器会将 "G" 解释为字符串 "G"、"()" 解释为字符串 "o" ，"(al)" 解释为字符串 "al" 。
 * 然后，按原顺序将经解释得到的字符串连接成一个字符串。
 * 给你字符串 command ，返回 Goal 解析器 对 command 的解释结果。
 * 提示：
 * 1、1 <= command.length <= 100
 * 2、command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成
 * 链接：https://leetcode-cn.com/problems/goal-parser-interpretation
 */
public class Q1678 {

    public static void main(String[] args) {
        // Goal
        System.out.println(new Q1678().interpret("G()(al)"));
        // Gooooal
        System.out.println(new Q1678().interpret("G()()()()(al)"));
        // alGalooG
        System.out.println(new Q1678().interpret("(al)G(al)()()G"));
    }

    public String interpret(String command) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < command.length(); i++) {
            char c = command.charAt(i);
            if (c == 'G') sb.append("G");
            else if (c == ')') sb.append("o");
            else if (c == 'a') {
                sb.append("al");
                i += 2;
            }
        }
        return sb.toString();
    }
}
