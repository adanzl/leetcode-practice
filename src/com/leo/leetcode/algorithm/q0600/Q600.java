package com.leo.leetcode.algorithm.q0600;

/**
 * 给定一个正整数 n ，返回范围在 [0, n] 都非负整数中，其二进制表示不包含 连续的 1 的个数。
 * 提示: 1 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/
 */
public class Q600 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q600().findIntegers(3));
        // 514229
        System.out.println(new Q600().findIntegers(100_000_001));
        // 5
        System.out.println(new Q600().findIntegers(5));
        // 4
        System.out.println(new Q600().findIntegers(4));
        // 3
        System.out.println(new Q600().findIntegers(2));
        // 2
        System.out.println(new Q600().findIntegers(1));
        // 6
        System.out.println(new Q600().findIntegers(8));
        // 9
        System.out.println(new Q600().findIntegers(16));
    }

    static int[][] dp = new int[33][];

    static {
        dp[0] = new int[]{1, 1};
        for (int i = 1; i < 33; i++) dp[i] = new int[]{dp[i - 1][0] + dp[i - 1][1], dp[i - 1][0]};
    }

    public int findIntegers(int n) {
        int ret = 0, pre = -1;
        for (int i = 32; i > 0; i--) {
            int sign = 1 & (n >> (i - 1));
            if (sign == 1) ret += dp[i - 1][0];
            if (sign == 1 && pre == sign) break;
            pre = sign;
            if (i == 1) ret++;
        }
        return ret;
    }
}
