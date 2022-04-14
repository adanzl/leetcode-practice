package com.leo.leetcode.algorithm.q1600;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 你有一些球的库存 inventory ，里面包含着不同颜色的球。一个顾客想要 任意颜色 总数为 orders 的球。
 * 这位顾客有一种特殊的方式衡量球的价值：每个球的价值是目前剩下的 同色球 的数目。
 * 比方说还剩下 6 个黄球，那么顾客买第一个黄球的时候该黄球的价值为 6 。这笔交易以后，只剩下 5 个黄球了，所以下一个黄球的价值为 5 （也就是球的价值随着顾客购买同色球是递减的）
 * 给你整数数组 inventory ，其中 inventory[i] 表示第 i 种颜色球一开始的数目。同时给你整数 orders ，表示顾客总共想买的球数目。你可以按照 任意顺序 卖球。
 * 请你返回卖了 orders 个球以后 最大 总价值之和。由于答案可能会很大，请你返回答案对 109 + 7 取余数 的结果。
 * 提示：
 * 1、1 <= inventory.length <= 10^5
 * 2、1 <= inventory[i] <= 10^9
 * 3、1 <= orders <= min(sum(inventory[i]), 10^9)
 * 链接：https://leetcode-cn.com/problems/sell-diminishing-valued-colored-balls
 */
public class Q1648 {

    public static void main(String[] args) {
        // 21
        System.out.println(new Q1648().maxProfit(stringToIntegerArray("[1000000000]"), 1000000000));
        // 19
        System.out.println(new Q1648().maxProfit(stringToIntegerArray("[3,5]"), 6));
        // 14
        System.out.println(new Q1648().maxProfit(stringToIntegerArray("[2,5]"), 4));
        // 110
        System.out.println(new Q1648().maxProfit(stringToIntegerArray("[2,8,4,10,6]"), 20));
    }

    public int maxProfit(int[] inventory, int orders) {
        Arrays.sort(inventory);
        int n = inventory.length, MOD = 1_000_000_007, p1 = 0, p2 = n - 1;
        long[] preSum = new long[n + 1];
        for (int i = 0; i < n; i++) preSum[i + 1] = preSum[i] + inventory[i];
        long l = 0, r = inventory[n - 1], price = 0, sold = 0, ret = 0;
        while (l <= r) {
            long mid = l + (r - l) / 2;
            int idx = binarySearch(inventory, p1, p2, mid);
            long sells = preSum[n] - preSum[idx] - (n - idx) * (mid - 1);
            if (sells > orders) {
                l = mid + 1;
                p1 = idx;
            } else {
                r = mid - 1;
                price = mid;
                sold = sells;
                p2 = idx;
            }
        }
        for (int i = n - 1; i >= 0 && inventory[i] >= price; i--) {
            ret = (ret + (inventory[i] + price) * (inventory[i] - price + 1) / 2) % MOD;
        }
        ret = (ret + (orders - sold) * (price - 1)) % MOD;
        return (int) (ret % MOD);
    }

    int binarySearch(int[] arr, int l, int r, long target) {
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] >= target) r = mid - 1;
            else l = mid + 1;
        }
        return l;
    }
}
