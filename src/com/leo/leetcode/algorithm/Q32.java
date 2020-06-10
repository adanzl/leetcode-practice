package com.leo.leetcode.algorithm;

import java.util.Stack;

public class Q32 {
    public int longestValidParentheses(String s) {

        Stack<Integer> stack = new Stack<>();
        int[] flags = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            flags[i] = 0;
            char v = s.charAt(i);

            if (v == '(') {
                stack.push(i);
                flags[i] = 1;
            } else if (v == ')') {
                if (stack.empty()) {
                    flags[i] = 1;
                } else {
                    flags[stack.pop()] = 0;
                }
            }
        }

        int ret = 0;
        int len = 0;
        for (int i = 0; i < flags.length; i++) {
            if (flags[i] == 1) {
                len = 0;
            } else {
                len++;
                ret = Math.max(ret, len);
            }
        }
        return ret;
    }
}
