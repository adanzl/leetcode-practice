package com.leo.leetcode.algorithm.q0900;

public class Q983 {

    public static void main(String[] args) {
        System.out.println(new Q983().minCostTickets(new int[]{1, 4, 6, 7, 8, 20}, new int[]{7, 2, 15})); // 6
        System.out.println(new Q983().minCostTickets(new int[]{1, 4, 6, 7, 8, 20}, new int[]{2, 7, 15})); // 11
        System.out.println(new Q983().minCostTickets(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31}, new int[]{2, 7, 15})); // 17
    }

    public int minCostTickets(int[] days, int[] costs) {
        int endDay = days[days.length - 1], j = 0, limit = days[j];
        int[] dp = new int[endDay + 1];
        for (int i = 1; i < endDay + 1; i++) {
            if (i < limit) {
                dp[i] = dp[i - 1];
            } else {
                int c1 = dp[i - 1] + costs[0];
                int c7 = i > 7 ? dp[i - 7] + costs[1] : costs[1];
                int c30 = i > 30 ? dp[i - 30] + costs[2] : costs[2];
                dp[i] = Math.min(c1, Math.min(c7, c30));
                if (j < days.length - 1) limit = days[++j];
            }

        }

        return dp[endDay];
    }
}
