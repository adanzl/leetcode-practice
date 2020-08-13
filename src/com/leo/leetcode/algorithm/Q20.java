package com.leo.leetcode.algorithm;

/**
 * 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
 * 有效字符串需满足：
 *   左括号必须用相同类型的右括号闭合。
 *   左括号必须以正确的顺序闭合。
 *   注意空字符串可被认为是有效字符串。
 * 链接：https://leetcode-cn.com/problems/valid-parentheses
 */
public class Q20 {

    public static void main(String[] args) {
        System.out.println(new Q20().isValid("()")); // true
        System.out.println(new Q20().isValid("()[]{}")); // true
        System.out.println(new Q20().isValid("(]")); // false
        System.out.println(new Q20().isValid("([)]")); // false
        System.out.println(new Q20().isValid("{[]}")); // true
    }

    public boolean isValid(String s) {
        char[] stack = new char[s.length()];
        int index = 0;
        for (int i = 0; i < s.length(); i++) {
            char v = s.charAt(i);
            if (' ' == v) continue;
            if (v == '[' || v == '(' || v == '{') {
                stack[index++] = v;
            } else {
                if (index == 0) return false;
                char c = stack[--index];
                char r = ' ';
                if (c == '[') r = ']';
                else if (c == '{') r = '}';
                else if (c == '(') r = ')';
                if (r != v) return false;
            }
        }
        return index == 0;
    }
}
