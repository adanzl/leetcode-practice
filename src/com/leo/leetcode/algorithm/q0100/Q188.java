package com.leo.leetcode.algorithm.q0100;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
 * 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
 * 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 * <p>
 * 提示：
 * 1、0 <= k <= 100
 * 2、0 <= prices.length <= 1000
 * 3、0 <= prices[i] <= 1000
 * <p>
 * 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
 */
public class Q188 {

    public static void main(String[] args) {
        // 7
        System.out.println(new Q188().maxProfit(2, stringToIntegerArray("[3,2,6,5,0,3]")));
        // 17
        System.out.println(new Q188().maxProfit(2, stringToIntegerArray("[1,2,4,2,5,7,2,4,9,0,9]")));
        // 2
        System.out.println(new Q188().maxProfit(2, stringToIntegerArray("[2,4,1]")));
        // 7
        System.out.println(new Q188().maxProfit(2, stringToIntegerArray("[3,2,6,5,0,3]")));
        // 6
        System.out.println(new Q188().maxProfit(2, stringToIntegerArray("[3,3,5,0,0,3,1,4]")));
        // 3
        System.out.println(new Q188().maxProfit(2, stringToIntegerArray("[1,2,4]")));
        // 1
        System.out.println(new Q188().maxProfit1(1, stringToIntegerArray("[1,2]")));
        // 0
        System.out.println(new Q188().maxProfit1(0, stringToIntegerArray("[]")));
    }

    public int maxProfit1(int k, int[] prices) {
        if (k == 0 || prices.length == 0) return 0;
        int ret = 0, size = (k << 1) + 1;
        int[][] mark = new int[prices.length][size]; // * 标记的是状态，不是动作
        Arrays.fill(mark[0], Integer.MIN_VALUE >> 1);
        mark[0][0] = 0;
        mark[0][1] = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            Arrays.fill(mark[i], Integer.MIN_VALUE >> 1);
            for (int j = 0; j <= k; j++) mark[i][0] = Math.max(mark[i - 1][0], mark[i - 1][j << 1]);
            mark[i][1] = Math.max(mark[i - 1][1], -prices[i]);
            for (int j = 2; j < (Math.min(k, i) << 1) + 1; j++) {
                // j buy
                if ((j & 1) != 0) mark[i][j] = Math.max(mark[i - 1][j], mark[i - 1][j - 1] - prices[i]);
                else {
                    // j sell
                    mark[i][j] = Math.max(mark[i - 1][j - 1] + prices[i], mark[i - 1][j]);
                    ret = Math.max(ret, mark[i][j]);
                }
            }
        }
        return ret;
    }

    public int maxProfit(int k, int[] prices) {
        if (k == 0 || prices.length == 0) return 0;
        int ret = 0;
        // * 标记的是状态，不是动作
        int[] sells = new int[k + 1], buys = new int[k + 1];
        Arrays.fill(sells, Integer.MIN_VALUE >> 1);
        Arrays.fill(buys, Integer.MIN_VALUE >> 1);
        buys[0] = -prices[0];
        sells[0] = 0;
        for (int i = 1; i < prices.length; i++) {
            buys[0] = Math.max(buys[0], sells[0] - prices[i]);
            for (int j = 1; j <= Math.min(k, i); j++) {
                buys[j] = Math.max(buys[j], sells[j] - prices[i]); // buy
                sells[j] = Math.max(sells[j], buys[j - 1] + prices[i]);// sell
                ret = Math.max(ret, sells[j]);
            }
        }
        return ret;
    }
}
