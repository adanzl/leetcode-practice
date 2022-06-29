package com.leo.leetcode.algorithm.q2300;

/**
 * 一条街道上共有 n * 2 个 地块 ，街道的两侧各有 n 个地块。每一边的地块都按从 1 到 n 编号。每个地块上都可以放置一所房子。
 * 现要求街道同一侧不能存在两所房子相邻的情况，请你计算并返回放置房屋的方式数目。由于答案可能很大，需要对 10^9 + 7 取余后再返回。
 * 注意，如果一所房子放置在这条街某一侧上的第 i 个地块，不影响在另一侧的第 i 个地块放置房子。
 * 提示：1 <= n <= 10^4
 * 链接：https://leetcode.cn/problems/count-number-of-ways-to-place-houses
 */
public class Q2320 {

    public static void main(String[] args) {
        // 402613600
        System.out.println(new Q2320().countHousePlacements(10000));
        // 4
        System.out.println(new Q2320().countHousePlacements(1));
        // 9
        System.out.println(new Q2320().countHousePlacements(2));
    }

    public int countHousePlacements(int n) {
        int MOD = 1_000_000_007;
        long[][] dp = new long[n][2];
        dp[0][0] = 1;
        dp[0][1] = 1;
        for (int i = 1; i < n; i++) {
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD;
            dp[i][1] = dp[i - 1][0] % MOD;
        }
        long ret = dp[n - 1][0] + dp[n - 1][1];
        ret = (ret * ret) % MOD;
        return (int) (ret % MOD);
    }

}
