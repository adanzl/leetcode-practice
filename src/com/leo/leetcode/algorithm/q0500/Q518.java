package com.leo.leetcode.algorithm.q0500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
 * 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
 * 假设每一种面额的硬币有无限个。
 * 题目数据保证结果符合 32 位带符号整数。
 * 提示：
 * 1、1 <= coins.length <= 300
 * 2、1 <= coins[i] <= 5000
 * 3、coins 中的所有值 互不相同
 * 4、0 <= amount <= 5000
 * <p>
 * 链接：https://leetcode-cn.com/problems/coin-change-2
 */
public class Q518 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q518().change(5, stringToIntegerArray("[1, 2, 5]")));
        // 0
        System.out.println(new Q518().change(3, stringToIntegerArray("[2]")));
        // 1
        System.out.println(new Q518().change(10, stringToIntegerArray("[10]")));
        // 1
        System.out.println(new Q518().change(0, stringToIntegerArray("[1, 2, 5]")));
    }

    public int change(int amount, int[] coins) {
        if (amount == 0) return 1;
        int[] dp = new int[amount + 1];
        for (int c : coins) {
            if (c <= amount) ++dp[c];
            for (int j = c; j <= amount; j++) dp[j] += dp[j - c];
        }
        return dp[amount];
    }

}
