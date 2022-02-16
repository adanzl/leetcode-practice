package com.leo.leetcode.algorithm.q0200;

import java.util.Stack;

/**
 * 实现一个基本的计算器来计算一个简单的字符串表达式的值。
 * 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格。 整数除法仅保留整数部分。
 * 说明：
 * 1、你可以假设所给定的表达式都是有效的。
 * 2、请不要使用内置的库函数 eval。
 */

public class Q227 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q227().calculate("1-1+1"));
        // 7
        System.out.println(new Q227().calculate("3+2*2"));
        // 10
        System.out.println(new Q227().calculate("3 +2 *2+1* 2+1"));
        // 1
        System.out.println(new Q227().calculate(" 3/ 2 "));
        // 5
        System.out.println(new Q227().calculate(" 3+5 / 2 "));
    }

    public int calculate(String s) {
        int num = 0;
        Stack<Character> signs = new Stack<>();
        Stack<Integer> ret = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ' ') continue;
            if (c >= '0' && c <= '9') {
                num = num * 10 + c - '0';
            } else {
                ret.push(num);
                num = 0;
                popSign(signs, ret, c);
                signs.push(c);
            }
        }
        ret.push(num);
        popSign(signs, ret, ' ');
        return ret.pop();
    }

    void popSign(Stack<Character> signs, Stack<Integer> ret, char c) {
        while (!signs.empty() && getPriority(signs.peek()) >= getPriority(c)) {
            char sign = signs.pop();
            int p1 = ret.pop(), p2 = ret.pop(), v = 0;
            if (sign == '+') v = p1 + p2;
            else if (sign == '-') v = p2 - p1;
            else if (sign == '*') v = p2 * p1;
            else if (sign == '/') v = p2 / p1;
            ret.push(v);
        }
    }

    int getPriority(char sign) {
        if (sign == '-' || sign == '+') return 1;
        if (sign == '*' || sign == '/') return 2;
        return -1;
    }

}
