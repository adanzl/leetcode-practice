package com.leo.leetcode.algorithm.q0000;

/**
 * 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
 * 返回被除数 dividend 除以除数 divisor 得到的商。
 * 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
 * <p>
 * 提示：
 * 1、被除数和除数均为 32 位有符号整数。
 * 2、除数不为 0。
 * 3、假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
 * <p>
 * 链接：https://leetcode-cn.com/problems/divide-two-integers
 */
public class Q29 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q29().divide(Integer.MIN_VALUE, Integer.MIN_VALUE));
        // 715827882
        System.out.println(new Q29().divide(Integer.MAX_VALUE, 3));
        // -2
        System.out.println(new Q29().divide(7, -3));
        // 2147483647
        System.out.println(new Q29().divide(Integer.MIN_VALUE, -1));
        // 1073741824
        System.out.println(new Q29().divide(Integer.MIN_VALUE, -2));
        // 3
        System.out.println(new Q29().divide(10, 3));
    }

    public int divide(int dividend, int divisor) {
        int sign = 1, flag = (dividend > 0) ^ (divisor > 0) ? -1 : 1;
        long ret = 0, d1 = Math.abs((long) dividend), d2 = Math.abs((long) divisor);
        while (d2 << sign <= d1) sign++;
        sign--;
        while (d1 >= d2) {
            if (d1 >= d2 << sign) {
                ret += 1L << sign;
                d1 -= d2 << sign;
            }
            sign--;
        }
        ret *= flag;
        return ret > Integer.MAX_VALUE ? Integer.MAX_VALUE : (int) ret;
    }
}
