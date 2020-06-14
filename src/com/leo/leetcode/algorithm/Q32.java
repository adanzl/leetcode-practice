package com.leo.leetcode.algorithm;

import java.util.Stack;

/**
 * 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
 * 链接：https://leetcode-cn.com/problems/longest-valid-parentheses
 */
public class Q32 {

    public static void main(String[] args) {
        System.out.println(new Q32().longestValidParentheses("(()")); // 2
        System.out.println(new Q32().longestValidParentheses(")()())")); // 4
    }

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
                if (stack.empty()) flags[i] = 1;
                else flags[stack.pop()] = 0;
            }
        }

        int ret = 0, len = 0;
        for (int flag : flags) {
            if (flag == 1) {
                len = 0;
            } else {
                len++;
                ret = Math.max(ret, len);
            }
        }
        return ret;
    }
}
