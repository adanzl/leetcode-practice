package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

public class Q121 {
    @Test
    public void TestOJ() {
        System.out.println(maxProfit(LCUtil.stringToIntegerArray("[7,1,5,3,6,4]")));
    }

    public int maxProfit(int[] prices) {
        // minPrice 和 maxProfit，分别对应[迄今为止]所得到的最小的谷值和最大的利润
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } else if (prices[i] - minPrice > maxProfit) {
                maxProfit = prices[i] - minPrice;
            }
        }
        return maxProfit;
    }
}
