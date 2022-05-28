package com.leo.leetcode.algorithm.q1000;

/**
 * 有效括号字符串为空 ""、"(" + A + ")" 或 A + B ，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。
 * 例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
 * 如果有效字符串 s 非空，且不存在将其拆分为 s = A + B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
 * 给出一个非空有效字符串 s，考虑将其进行原语化分解，使得：s = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
 * 对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 为 '(' 或 ')'
 * s 是一个有效括号字符串
 * 链接：https://leetcode.cn/problems/remove-outermost-parentheses
 */
public class Q1021 {

    public static void main(String[] args) {

        // "()()()"
        System.out.println(new Q1021().removeOuterParentheses("(()())(())"));
        // "()()()()(())"
        System.out.println(new Q1021().removeOuterParentheses("(()())(())(()(()))"));
        // ""
        System.out.println(new Q1021().removeOuterParentheses("()()"));
    }

    public String removeOuterParentheses(String s) {
        StringBuilder ret = new StringBuilder();
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                if (count > 0) ret.append(c);
                count++;
            } else {
                count--;
                if (count > 0) ret.append(c);
            }
        }
        return ret.toString();
    }
}