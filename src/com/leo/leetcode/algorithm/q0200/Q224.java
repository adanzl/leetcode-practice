package com.leo.leetcode.algorithm.q0200;

import java.util.Stack;

/**
 * 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
 * 提示：
 * 1、1 <= s.length <= 3 * 10^5
 * 2、s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
 * 3、s 表示一个有效的表达式
 * 链接：https://leetcode-cn.com/problems/basic-calculator/
 */
public class Q224 {

    public static void main(String[] args) {
        // -12
        System.out.println(new Q224().calculate("- (3 + (4 + 5))"));
        // 18 这个用例官方答案错了，官方答案是 11
        System.out.println(new Q224().calculate("(1+((4+5)*2)-3)+(-6+8)"));
        // 11
        System.out.println(new Q224().calculate("(1+(4+5+2)-3)+(-6+8)"));
        // -3
        System.out.println(new Q224().calculate("-2 + -1"));
        // 2
        System.out.println(new Q224().calculate("1 + 1"));
        // 3
        System.out.println(new Q224().calculate(" 2-1 + 2 "));
    }

    public int calculate(String s) {
        int num = 0, sign = 1;
        boolean bPreNum = false, bPreSign = true;
        Stack<Character> operators = new Stack<>();
        Stack<Integer> ret = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ' ') continue;
            if (c >= '0' && c <= '9') {
                bPreSign = false;
                if (bPreNum) {
                    num = num * 10 + c - '0';
                    sign = 1;
                } else {
                    num = (c - '0') * sign;
                    bPreNum = true;
                }
            } else {
                if (bPreNum) {
                    ret.push(num);
                    bPreNum = false;
                    sign = 1;
                }
                if (c != '(' && c != ')') {
                    if (bPreSign) {
                        sign = c == '-' ? -1 : 1;
                        continue;
                    }
                    bPreSign = true;
                }
                if (bPreSign || c == '(') {
                    operators.push('*');
                    ret.push(sign);
                    sign = 1;
                }
                popOpt(operators, ret, c);
                if (c != ')') operators.push(c);
            }
        }
        if (bPreNum) ret.push(num);
        popOpt(operators, ret, ' ');
        return ret.pop();
    }

    void popOpt(Stack<Character> operators, Stack<Integer> ret, char c) {
        while (!operators.empty() && getPriority(operators.peek()) >= getPriority(c)) {
            if (operators.peek() == '(' && c != ')') break;
            char opt = operators.pop();
            if (opt == '(') break;
            int p1 = ret.pop(), p2 = ret.pop(), v = 0;
            if (opt == '+') v = p1 + p2;
            else if (opt == '-') v = p2 - p1;
            else if (opt == '*') v = p2 * p1;
            else if (opt == '/') v = p2 / p1;
            ret.push(v);
        }
    }

    int getPriority(char sign) {
        if (sign == '(') return 3;
        if (sign == ')') return 0;
        if (sign == '-' || sign == '+') return 1;
        if (sign == '*' || sign == '/') return 2;
        return -1;
    }

}
