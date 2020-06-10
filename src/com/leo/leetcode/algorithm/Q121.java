package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q121 {

    public static void main(String[] args) {
        new Q121().TestOJ();
    }

    public void TestOJ() {
        System.out.println(maxProfit(LCUtil.stringToIntegerArray("[7,1,5,3,6,4]")));
    }

    public int maxProfit(int[] prices) {
        // minPrice 和 maxProfit，分别对应[迄今为止]所得到的最小的谷值和最大的利润
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        return maxProfit;
    }
}
