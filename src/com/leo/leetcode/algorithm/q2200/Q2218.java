package com.leo.leetcode.algorithm.q2200;

import java.util.List;

import static com.leo.utils.LCUtil.stringToListListInt;

/**
 * 一张桌子上总共有 n个硬币 栈 。每个栈有 正整数 个带面值的硬币。
 * 每一次操作中，你可以从任意一个栈的 顶部 取出 1 个硬币，从栈中移除它，并放入你的钱包里。
 * 给你一个列表 piles ，其中 piles[i] 是一个整数数组，分别表示第 i 个栈里 从顶到底 的硬币面值。
 * 同时给你一个正整数 k ，请你返回在 恰好 进行 k 次操作的前提下，你钱包里硬币面值之和 最大为多少 。
 * 提示：
 * 1、n == piles.length
 * 2、1 <= n <= 1000
 * 3、1 <= piles[i][j] <= 10^5
 * 4、1 <= k <= sum(piles[i].length) <= 2000
 * 链接：https://leetcode-cn.com/problems/maximum-value-of-k-coins-from-piles
 */
public class Q2218 {

    public static void main(String[] args) {
        // 494
        System.out.println(new Q2218().maxValueOfCoins(stringToListListInt("[[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]]"), 9));
        // 706
        System.out.println(new Q2218().maxValueOfCoins(stringToListListInt("[[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]"), 7));
        // 101
        System.out.println(new Q2218().maxValueOfCoins(stringToListListInt("[[1,100,3],[7,8,9]]"), 2));
    }

    public int maxValueOfCoins(List<List<Integer>> piles, int k) {
        int n = piles.size();
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 1; i <= n; i++) {
            int size = piles.get(i - 1).size();
            int[] preSum = new int[size + 1];
            for (int j = 1; j <= size; j++) preSum[j] = preSum[j - 1] + piles.get(i - 1).get(j - 1);
            for (int j = 1; j <= k; j++) {
                dp[i][j] = dp[i - 1][j];
                for (int l = 1; l <= size && l <= j; l++) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - l] + preSum[l]);
                }
            }
        }
        return dp[n][k];
    }
}
