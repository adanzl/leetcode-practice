package com.leo.leetcode.algorithm.q0600;

/**
 * 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
 * 提示： 0 <= c <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/sum-of-square-numbers/
 */
public class Q633 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q633().judgeSquareSum(5));
        // false
        System.out.println(new Q633().judgeSquareSum(3));
    }

    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            double b = Math.sqrt(c - a * a);
            if (b == (int) b) return true;
        }
        return false;
    }

}
