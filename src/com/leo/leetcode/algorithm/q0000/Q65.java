package com.leo.leetcode.algorithm.q0000;

/**
 * 有效数字（按顺序）可以分成以下几个部分：
 * 1、一个 小数 或者 整数
 * 2、（可选）一个 'e' 或 'E' ，后面跟着一个 整数
 * 小数（按顺序）可以分成以下几个部分：
 * 1、（可选）一个符号字符（'+' 或 '-'）
 * 2、下述格式之一：
 * （1）、至少一位数字，后面跟着一个点 '.'
 * （2）、至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
 * （3）、一个点 '.' ，后面跟着至少一位数字
 * 整数（按顺序）可以分成以下几个部分：
 * 1、（可选）一个符号字符（'+' 或 '-'）
 * 2、至少一位数字
 * 部分有效数字列举如下：
 * # ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
 * 部分无效数字列举如下：
 * # ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
 * 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
 * <p>
 * 提示：
 * 1、1 <= s.length <= 20
 * 2、s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
 * <p>
 * 链接：https://leetcode-cn.com/problems/valid-number
 */
public class Q65 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q65().isNumber("005047e+6"));
        // true
        System.out.println(new Q65().isNumber("09"));
        // true
        System.out.println(new Q65().isNumber("+.9"));
        // true
        System.out.println(new Q65().isNumber("-9."));
        // true
        System.out.println(new Q65().isNumber("2.E+10"));
        // true
        System.out.println(new Q65().isNumber("+6e-1"));
        // false
        System.out.println(new Q65().isNumber("a"));
        // false
        System.out.println(new Q65().isNumber("1e"));
        // false
        System.out.println(new Q65().isNumber("e3"));
        // false
        System.out.println(new Q65().isNumber("--6"));
        // false
        System.out.println(new Q65().isNumber("99e2.5"));
        // false
        System.out.println(new Q65().isNumber("3e3e1"));
        // false
        System.out.println(new Q65().isNumber("3.3.1"));
        // false
        System.out.println(new Q65().isNumber(".-3"));
    }

    public boolean isNumber(String s) {
        boolean bSign = false, bE = false, bDot = false, bNum = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                bNum = true;
            } else if (c == 'e' || c == 'E') {
                if (bE || !bNum) return false;
                bE = true;
                bSign = false;
                bNum = false;
            } else if (c == '-' || c == '+') {
                if (bSign || bNum || (bDot && !bE)) return false;
                bSign = true;
            } else if (c == '.') {
                if (bDot || bE) return false;
                bDot = true;
            } else return false;
        }
        return bNum;
    }
}
