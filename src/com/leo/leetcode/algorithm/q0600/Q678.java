package com.leo.leetcode.algorithm.q0600;

import java.util.Deque;
import java.util.LinkedList;

/**
 * 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
 * 1、任何左括号 ( 必须有相应的右括号 )。
 * 2、任何右括号 ) 必须有相应的左括号 ( 。
 * 3、左括号 ( 必须在对应的右括号之前 )。
 * 4、* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
 * 5、一个空字符串也被视为有效字符串。
 * 注意: 字符串大小将在 [1，100] 范围内。
 * 链接：https://leetcode.cn/problems/valid-parenthesis-string
 */
public class Q678 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q678().checkValidString("(*)"));
        // true
        System.out.println(new Q678().checkValidString("()"));
        // true
        System.out.println(new Q678().checkValidString("(*))"));
    }

    public boolean checkValidString(String s) {
        Deque<Integer> starStack = new LinkedList<>(), lStack = new LinkedList<>();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '(') lStack.push(i);
            else if (c == '*') starStack.push(i);
            else {
                if (lStack.isEmpty() && starStack.isEmpty()) return false;
                if (!lStack.isEmpty()) lStack.pop();
                else starStack.pop();
            }
        }
        while (!lStack.isEmpty()) {
            int il = lStack.pop();
            if (starStack.isEmpty() || il > starStack.pop()) return false;
        }
        return true;
    }
}
