package com.leo.leetcode.algorithm.q0100;

/**
 * 给定一个整数 n，返回 n! 结果尾数中零的数量。
 * 说明: 你算法的时间复杂度应为 O(log n) 。
 * <p>
 * 链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes/
 */
public class Q172 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q172().trailingZeroes(3));
        // 1
        System.out.println(new Q172().trailingZeroes(5));
        // 7
        System.out.println(new Q172().trailingZeroes(99));
    }

    public int trailingZeroes(int n) {
        int ret = 0, sign = 5;
        while (sign <= n) {
            ret += n / sign;
            sign *= 5;
        }
        return ret;
    }
}
