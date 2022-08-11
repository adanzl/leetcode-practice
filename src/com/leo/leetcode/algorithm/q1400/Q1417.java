package com.leo.leetcode.algorithm.q1400;

/**
 * 给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。
 * 请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。
 * 请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。
 * 提示：
 * 1、1 <= s.length <= 500
 * 2、s 仅由小写英文字母和/或数字组成。
 * 链接：https://leetcode.cn/problems/reformat-the-string
 */
public class Q1417 {

    public static void main(String[] args) {
        // "0a1b2c"
        System.out.println(new Q1417().reformat("a0b1c2"));
        // ""
        System.out.println(new Q1417().reformat("leetcode"));
        // ""
        System.out.println(new Q1417().reformat("1229857369"));
        // "c2o0v1i9d"
        System.out.println(new Q1417().reformat("covid2019"));
        // "1a2b3"
        System.out.println(new Q1417().reformat("ab123"));
    }

    public String reformat(String s) {
        int cDigit = 0, cCh = 0, id, ic;
        char[] str = s.toCharArray();
        for (char c : str) {
            if (Character.isDigit(c)) cDigit++;
            else cCh++;
        }
        if (Math.abs(cDigit - cCh) > 1) return "";
        if (cDigit > cCh) {
            id = 0;
            ic = 1;
        } else {
            id = 1;
            ic = 0;
        }
        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) {
                str[id] = s.charAt(i);
                id += 2;
            } else {
                str[ic] = s.charAt(i);
                ic += 2;
            }
        }
        return new String(str);
    }
}
