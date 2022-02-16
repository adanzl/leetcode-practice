package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
 * 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
 * 返回获得利润的最大值。
 * 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
 * 提示：
 * 1、1 <= prices.length <= 5 * 10^4
 * 2、1 <= prices[i] < 5 * 10^4
 * 3、0 <= fee < 5 * 10^4
 * 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
 */
public class Q714 {

    public static void main(String[] args) {
        // 8
        System.out.println(new Q714().maxProfit(stringToIntegerArray("[1,3,2,8,4,9]"), 2));
        // 6
        System.out.println(new Q714().maxProfit(stringToIntegerArray("[1,3,7,5,10,3]"), 3));
    }

    public int maxProfit(int[] prices, int fee) {
        int ret = 0;
        int[] flag = new int[]{-prices[0], 0}; // hold-none
        for (int price : prices) {
            int v0 = flag[0], v1 = flag[1];
            flag[0] = Math.max(v0, v1 - price);
            flag[1] = Math.max(v0 + price - fee, v1);
            for (int v : flag) ret = Math.max(ret, v);
        }
        return ret;
    }
}
