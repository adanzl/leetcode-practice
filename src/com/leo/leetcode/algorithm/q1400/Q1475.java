package com.leo.leetcode.algorithm.q1400;

import java.util.Arrays;

/**
 * 给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
 * 商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，
 * 其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。
 * 请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。
 * 提示：
 * 1、1 <= prices.length <= 500
 * 2、1 <= prices[i] <= 10^3
 * 链接：https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop
 */
public class Q1475 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q1475().finalPrices(new int[]{8, 4, 6, 2, 3}))); // [4,2,4,2,3]
        System.out.println(Arrays.toString(new Q1475().finalPrices(new int[]{1, 2, 3, 4, 5}))); // [1,2,3,4,5]
        System.out.println(Arrays.toString(new Q1475().finalPrices(new int[]{10, 1, 1, 6}))); // [9,0,1,6]
    }

    public int[] finalPrices(int[] prices) {
        int[] out = new int[prices.length], stack = new int[prices.length];
        for (int i = prices.length - 1, j = 0; i >= 0; i--) {
            while (j > 0 && prices[stack[j - 1]] > prices[i]) j--;
            if (j > 0) out[i] = prices[i] - prices[stack[j - 1]];
            else out[i] = prices[i];
            stack[j++] = i;
        }
        return out;
    }
}
