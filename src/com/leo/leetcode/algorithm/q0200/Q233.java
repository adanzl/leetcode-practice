package com.leo.leetcode.algorithm.q0200;

/**
 * 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
 * 提示： 0 <= n <= 2 * 10^9
 * 链接：https://leetcode-cn.com/problems/number-of-digit-one/
 */
public class Q233 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q233().countDigitOne(13));
        // 0
        System.out.println(new Q233().countDigitOne(0));
    }

    // 使用数学方法，没意思
    int countDigitOne(int n) {
        int c = 0;
        for (long i = 1; i <= n; i *= 10) {
            long divider = i * 10;
            c += (n / divider) * i + Math.min(Math.max(n % divider - i + 1, 0L), i);
        }
        return c;
    }
}
