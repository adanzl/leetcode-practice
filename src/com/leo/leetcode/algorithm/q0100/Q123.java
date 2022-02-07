package com.leo.leetcode.algorithm.q0100;

/**
 * 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
 * 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
 * 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 * 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
 */
public class Q123 {
    public static void main(String[] args) {
        System.out.println(new Q123().maxProfit(new int[]{3, 3, 5, 0, 0, 3, 1, 4})); // 6
        System.out.println(new Q123().maxProfit(new int[]{1, 2, 3, 4, 5})); // 4
        System.out.println(new Q123().maxProfit(new int[]{7, 6, 4, 3, 1})); // 0
    }

    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        int[] mark = new int[prices.length];
        int max = 0, min_price = prices[0], out = 0;
        for (int i = 0; i < prices.length; i++) {
            min_price = Math.min(min_price, prices[i]);
            max = Math.max(max, prices[i] - min_price);
            mark[i] = max;
        }
        max = 0;
        int max_price = prices[prices.length - 1];
        for (int i = prices.length - 1; i >= 0; i--) {
            max_price = Math.max(max_price, prices[i]);
            max = Math.max(max, max_price - prices[i]);
            out = Math.max(out, mark[i] + max);
        }
        return out;
    }
}
