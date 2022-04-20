package com.leo.leetcode.algorithm.q0400;

/**
 * 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
 * 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。
 * 提示：1 <= n <= 2^31 - 1
 * 链接：https://leetcode-cn.com/problems/arranging-coins
 */
public class Q441 {

    public static void main(String[] args) {
        // 60070
        System.out.println(new Q441().arrangeCoins(1804289383));
        // 65535
        System.out.println(new Q441().arrangeCoins(Integer.MAX_VALUE));
        // 2
        System.out.println(new Q441().arrangeCoins(5));
        // 3
        System.out.println(new Q441().arrangeCoins(8));
    }

    public int arrangeCoins(int n) {
        int l = 1, r = 65535;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            long sum = (long) mid * (mid + 1) / 2;
            if (sum <= n) l = mid + 1;
            else r = mid - 1;
        }
        return l - 1;
    }
}
