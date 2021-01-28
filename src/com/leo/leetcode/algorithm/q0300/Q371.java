package com.leo.leetcode.algorithm.q0300;

/**
 * 不使用运算符 + 和 - ，计算两整数 a 、b 之和。
 *
 * 链接：https://leetcode-cn.com/problems/sum-of-two-integers/
 */
public class Q371 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q371().getSum(1, 2));
        // 1
        System.out.println(new Q371().getSum(-2, 3));
        // 8
        System.out.println(new Q371().getSum(7, 1));
    }

    int getSum(int a, int b) {
        if ((a & b) == 0) return a ^ b;    // 当进位为0时，返回两数相加不进位的加法结果
        return getSum(a ^ b, ((a & b)) << 1);    // 否则，递归计算不进位加法结果与进位之和
    }
}
