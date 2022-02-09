package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
 * 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
 * 请你计算并返回达到楼梯顶部的最低花费。
 * 提示：
 * 1、2 <= cost.length <= 1000
 * 2、0 <= cost[i] <= 999
 * 链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
 */
public class Q746 {
    public static void main(String[] args) {
        // 15
        System.out.println(new Q746().minCostClimbingStairs(stringToIntegerArray("[10,15,20]")));
        // 6
        System.out.println(new Q746().minCostClimbingStairs(stringToIntegerArray("[1,100,1,1,1,100,1,1,100,1]")));
    }

    public int minCostClimbingStairs(int[] cost) {
        int[] price = new int[2];
        for (int i = 2; i <= cost.length; i++) {
            int p = Math.min(price[0] + cost[i - 2], price[1] + cost[i - 1]);
            price[0] = price[1];
            price[1] = p;
        }
        return price[1];
    }
}
