package com.leo.leetcode.algorithm.q0300;

/**
 * 给定一个正整数 n ，你可以做如下操作：
 * 1、如果 n 是偶数，则用 n / 2替换 n 。
 * 2、如果 n 是奇数，则可以用 n + 1或 n - 1替换 n 。
 * 返回 n 变为 1 所需的 最小替换次数 。
 * 提示：1 <= n <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/integer-replacement
 */
public class Q397 {

    public static void main(String[] args) {
        // 32
        System.out.println(new Q397().integerReplacement(2147483647));
        // 2
        System.out.println(new Q397().integerReplacement(4));
        // 12
        System.out.println(new Q397().integerReplacement(1000));
        // 17
        System.out.println(new Q397().integerReplacement(65535));
        // 3
        System.out.println(new Q397().integerReplacement(8));
        // 4
        System.out.println(new Q397().integerReplacement(7));
    }

    public int integerReplacement(int n) {
        return func(n);
    }

    int func(long n) {
        if (n == 1) return 0;
        if ((n & 1) == 1) return Math.min(func(n + 1), func(n - 1)) + 1;
        return func(n / 2) + 1;
    }
}
