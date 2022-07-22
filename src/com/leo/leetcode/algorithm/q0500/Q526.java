package com.leo.leetcode.algorithm.q0500;

/**
 * 假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列 ：
 * 1、perm[i] 能够被 i 整除
 * 2、i 能够被 perm[i] 整除
 * 给你一个整数 n ，返回可以构造的 优美排列 的 数量 。
 * 提示：1 <= n <= 15
 * 链接：https://leetcode.cn/problems/beautiful-arrangement
 */
public class Q526 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q526().countArrangement(2));
        // 1
        System.out.println(new Q526().countArrangement(1));
        // 24679
        System.out.println(new Q526().countArrangement(15));
    }

    // 状态dp
    public int countArrangement(int n) {
        int size = 1 << n;
        int[] dp = new int[size];
        dp[0] = 1;
        for (int mask = 1; mask < size; mask++) {
            int count = Integer.bitCount(mask);
            for (int j = 0; j < n; j++) {
                if ((1 << j & mask) == 0) continue;
                if ((j + 1) % count != 0 && count % (j + 1) != 0) continue;
                dp[mask] += dp[mask ^ (1 << j)];
            }
        }
        return dp[size - 1];
    }
}
