package com.leo.leetcode.algorithm.q2300;

/**
 * 在第 1 天，有一个人发现了一个秘密。
 * 给你一个整数 delay ，表示每个人会在发现秘密后的 delay 天之后，每天 给一个新的人 分享 秘密。
 * 同时给你一个整数 forget ，表示每个人在发现秘密 forget 天之后会 忘记 这个秘密。一个人 不能 在忘记秘密那一天及之后的日子里分享秘密。
 * 给你一个整数 n ，请你返回在第 n 天结束时，知道秘密的人数。由于答案可能会很大，请你将结果对 109 + 7 取余 后返回。
 * 提示：
 * 1、2 <= n <= 1000
 * 2、1 <= delay < forget <= n
 * 链接：https://leetcode.cn/problems/number-of-people-aware-of-a-secret
 */
public class Q2327 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q2327().peopleAwareOfSecret(4, 1, 3));
        // 5
        System.out.println(new Q2327().peopleAwareOfSecret(6, 2, 4));
    }

    public int peopleAwareOfSecret(int n, int delay, int forget) {
        int MOD = 1_000_000_007;
        long[] dp = new long[forget];
        dp[0] = 1;
        for (int i = 0; i < n - 1; i++) {
            long[] newDp = new long[forget];
            for (int j = 0; j < dp.length; j++) {
                if (j >= delay - 1 && j < forget - 1) newDp[0] = (newDp[0] + dp[j]) % MOD;
                if (j > 0) newDp[j] = dp[j - 1];
            }
            dp = newDp;
        }
        long ret = 0;
        for (long num : dp) ret = (ret + num) % MOD;
        return (int) ret;
    }
}
