package com.leo.leetcode.algorithm.q0600;

/**
 * 给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。
 * 逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。
 * 由于答案可能很大，只需要返回 答案 mod 10^9 + 7 的值。
 * 说明: n 的范围是 [1, 1000] 并且 k 的范围是 [0, 1000]。
 * 链接：https://leetcode.cn/problems/k-inverse-pairs-array
 */
public class Q629 {

    public static void main(String[] args) {
        // 21670
        System.out.println(new Q629().kInversePairs(10, 10));
        // 106447125
        System.out.println(new Q629().kInversePairs(20, 20));
        // 959322173
        System.out.println(new Q629().kInversePairs(100, 100));
        // 2
        System.out.println(new Q629().kInversePairs(3, 1));
        // 1
        System.out.println(new Q629().kInversePairs(3, 0));
        // 663677020
        System.out.println(new Q629().kInversePairs(1000, 1000));
    }


    public int kInversePairs(int n, int k) {
        int MOD = 1_000_000_007;
        long[][] dp = new long[n + 1][k + 1];
        dp[0][0] = 1;
        dp[1][0] = 1;
        for (int i = 2; i <= n; i++) { // insert num
            for (int j = 1; j <= i; j++) { // insert pos
                int len = i - j;
                for (int l = 0; l + len < k + 1; l++) {
                    dp[i][l + len] += dp[i - 1][l];
                    dp[i][l + len] %= MOD;
                }
            }
        }
        return (int) dp[n][k];
    }
}
