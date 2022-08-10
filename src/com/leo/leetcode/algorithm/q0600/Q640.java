package com.leo.leetcode.algorithm.q0600;

/**
 * 求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。
 * 如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。
 * 题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。
 * 提示:
 * 1、3 <= equation.length <= 1000
 * 2、equation 只有一个 '='.
 * 3、equation 方程由整数组成，其绝对值在 [0, 100] 范围内，不含前导零和变量 'x' 。
 * 链接：https://leetcode.cn/problems/solve-the-equation
 */
public class Q640 {

    public static void main(String[] args) {
        // "Infinite solutions"
        System.out.println(new Q640().solveEquation("0x=0"));
        // "x=2"
        System.out.println(new Q640().solveEquation("2=x"));
        // "No solution"
        System.out.println(new Q640().solveEquation("0=1"));
        // "x=2"
        System.out.println(new Q640().solveEquation("x+5-3+x=6+x-2"));
        // "Infinite solutions"
        System.out.println(new Q640().solveEquation("x=x"));
        // "x=0"
        System.out.println(new Q640().solveEquation("2x=x"));
    }

    public String solveEquation(String equation) {
        int n = equation.length(), side = 1, xc = 0, num = 0, nn = 0, s = 1;
        for (int i = 0; i < n; i++) {
            char c = equation.charAt(i);
            if (c >= '0' && c <= '9') {
                nn = nn * 10 + c - '0';
            } else if (c == 'x') {
                if (i > 0 && Character.isDigit(equation.charAt(i - 1))) xc += s * side * nn;
                else xc += s * side;
                nn = 0;
                s = 1;
            } else {
                num += nn * s * side;
                nn = 0;
                s = 1;
            }
            if (c == '-') s = -1;
            else if (c == '=') side = -1;
        }
        num += nn * s * side;
        if (xc == 0) {
            return num == 0 ? "Infinite solutions" : "No solution";
        }
        return "x=" + -num / xc;
    }
}
