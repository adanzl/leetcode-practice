package com.leo.leetcode.algorithm;

import java.util.Stack;

public class Q150 {
    public void TestOJ() {
        System.out.println(evalRPN(new String[]{"2", "1", "+", "3", "*"})); // 9
        System.out.println(evalRPN(new String[]{"4", "13", "5", "/", "+"})); // 6
        System.out.println(evalRPN(new String[]{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"})); // 22
    }

    // +, -, *, /
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String s : tokens) {
            if (!isSign(s)) {
                stack.push(Integer.parseInt(s));
            } else {
                int v = calc(stack.pop(), stack.pop(), s);
                stack.push(v);
            }
        }
        return stack.pop();
    }

    private boolean isSign(String s) {
        return "+".equals(s) || "-".equals(s) || "*".equals(s) || "/".equals(s);
    }

    private int calc(int v2, int v1, String sign) {
        switch (sign) {
            case "+":
                return v1 + v2;
            case "-":
                return v1 - v2;
            case "*":
                return v1 * v2;
            case "/":
                return v1 / v2;
        }
        return 0;
    }
}
