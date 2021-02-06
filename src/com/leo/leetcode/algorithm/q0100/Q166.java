package com.leo.leetcode.algorithm.q0100;

import java.util.HashMap;
import java.util.Map;

/**
 * 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串 形式返回小数 。
 * 如果小数部分为循环小数，则将循环的部分括在括号内。
 * 如果存在多个答案，只需返回 任意一个 。
 * 对于所有给定的输入，保证 答案字符串的长度小于 10^4 。
 * <p>
 * 提示：
 * 1、-2^31 <= numerator, denominator <= 2^31 - 1
 * 2、denominator != 0
 * <p>
 * 链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
 */
public class Q166 {

    public static void main(String[] args) {
        // 0.1(6)
        System.out.println(new Q166().fractionToDecimal(1, 6));
        // 2147483648
        System.out.println(new Q166().fractionToDecimal(Integer.MIN_VALUE, -1));
        // 0.(012)
        System.out.println(new Q166().fractionToDecimal(4, 333));
        // 0
        System.out.println(new Q166().fractionToDecimal(0, 1));
        // 0.5
        System.out.println(new Q166().fractionToDecimal(1, 2));
        // 2
        System.out.println(new Q166().fractionToDecimal(2, 1));
        // 0.(6)
        System.out.println(new Q166().fractionToDecimal(2, 3));
        // 0.2
        System.out.println(new Q166().fractionToDecimal(-1, -5));
        // -0.2
        System.out.println(new Q166().fractionToDecimal(-1, 5));
    }

    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        Map<Long, Integer> remainMap = new HashMap<>();
        StringBuilder ret = new StringBuilder();
        if ((numerator > 0) ^ (denominator > 0)) ret.append("-");
        long num = Math.abs((long) numerator), denom = Math.abs((long) denominator);
        long remain = num % denom;
        ret.append(num / denom);
        if (remain != 0) ret.append(".");
        while (remain != 0) {
            if (remainMap.containsKey(remain)) {
                ret.insert(remainMap.get(remain), "(").append(")");
                return ret.toString();
            }
            remainMap.put(remain, ret.length());
            remain *= 10;
            ret.append(remain / denom);
            remain %= denom;
        }
        return ret.toString();
    }
}
