package com.leo.leetcode.algorithm.q1200;

import java.util.*;

/**
 * 给你一个由 '('、')' 和小写字母组成的字符串 s。
 * 你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
 * 请返回任意一个合法字符串。
 * 有效「括号字符串」应当符合以下 任意一条 要求：
 * 1、空字符串或只包含小写字母的字符串
 * 2、可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
 * 3、可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
 * 提示：
 * 1、1 <= s.length <= 105
 * 2、s[i] 可能是 '('、')' 或英文小写字母
 * 链接：https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses
 */
public class Q1249 {

    public static void main(String[] args) {
        // "lee(t(c)o)de"
        System.out.println(new Q1249().minRemoveToMakeValid("lee(t(c)o)de)"));
        // "ab(c)d"
        System.out.println(new Q1249().minRemoveToMakeValid("a)b(c)d"));
        // ""
        System.out.println(new Q1249().minRemoveToMakeValid("))(("));
    }

    public String minRemoveToMakeValid(String s) {
        StringBuilder ret = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        boolean[] flags = new boolean[s.length()];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') stack.push(i);
            if (c == ')') {
                if (stack.empty()) flags[i] = true;
                else stack.pop();
            }
        }
        while (!stack.empty()) flags[stack.pop()] = true;
        for (int i = 0; i < s.length(); i++) {
            if (flags[i]) continue;
            ret.append(s.charAt(i));
        }
        return ret.toString();
    }
}
