package com.leo.leetcode.algorithm.q0800;

public class Q837 {
    public static void main(String[] args) {
        System.out.println(new Q837().new21Game(6, 5, 3)); // 0.84774
        System.out.println(new Q837().new21Game(21, 17, 10)); // 0.73278
        System.out.println(new Q837().new21Game(6, 1, 10)); // 0.6
        System.out.println(new Q837().new21Game(10, 1, 10)); // 1.0
    }

    public double new21Game(int N, int K, int W) {
        // 先判断 K - 1 + W 是否在 N 的里面，如果在的话，说明肯定能赢得游戏，返回 1.0，也就是 100%
        if (N - K + 1 >= W) {
            return 1.0;
        }
        double[] dp = new double[K + W];
        // 将能赢得游戏的点数的概率设置为 1
        for (int i = K; i <= N; i++) {
            dp[i] = 1.0;
        }
        // 计算K + W 这几个点数的概率和
        double sumProb = N - K + 1;
        // 从 K - 1 开始计算，
        for (int i = K - 1; i >= 0; i--) {
            // 点数为 i 的赢得游戏的概率为 i + 1 ~ i + W 的概率和除以 W
            dp[i] = sumProb / W;
            sumProb = sumProb - dp[i + W] + dp[i];
        }

        return dp[0];
    }
}
