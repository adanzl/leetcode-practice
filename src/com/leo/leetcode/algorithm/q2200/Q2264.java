package com.leo.leetcode.algorithm.q2200;

/**
 * 给你一个字符串 num ，表示一个大整数。如果一个整数满足下述所有条件，则认为该整数是一个 优质整数 ：
 * 该整数是 num 的一个长度为 3 的 子字符串 。
 * 1、该整数由唯一一个数字重复 3 次组成。
 * 2、以字符串形式返回 最大的优质整数 。如果不存在满足要求的整数，则返回一个空字符串 "" 。
 * 注意：
 * 1、子字符串 是字符串中的一个连续字符序列。
 * 2、num 或优质整数中可能存在 前导零 。
 * 提示：
 * 1、3 <= num.length <= 1000
 * 2、num 仅由数字（0 - 9）组成
 * 链接：https://leetcode-cn.com/problems/largest-3-same-digit-number-in-string
 */
public class Q2264 {

    public static void main(String[] args) {
        // "888"
        System.out.println(new Q2264().largestGoodInteger("3200014888"));
        // "777"
        System.out.println(new Q2264().largestGoodInteger("6777133339"));
        // "000"
        System.out.println(new Q2264().largestGoodInteger("2300019"));
        // ""
        System.out.println(new Q2264().largestGoodInteger("42352338"));
    }

    public String largestGoodInteger(String num) {
        char[] str = num.toCharArray();
        if (str.length < 3) return "";
        int count = 1;
        char c = str[0], ret = ' ';
        for (int i = 1; i < str.length; i++) {
            if (str[i] == c) count++;
            else {
                c = str[i];
                count = 1;
            }
            if (count >= 3) ret = (char) Math.max(ret, c);
        }
        return ret == ' ' ? "" : String.valueOf(new char[]{ret, ret, ret});
    }
}
