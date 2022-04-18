package com.leo.leetcode.algorithm.q6000;

/**
 * 给你一个整数 total ，表示你拥有的总钱数。同时给你两个整数 cost1 和 cost2 ，分别表示一支钢笔和一支铅笔的价格。你可以花费你部分或者全部的钱，去买任意数目的两种笔。
 * 请你返回购买钢笔和铅笔的 不同方案数目 。
 * 提示： 1 <= total, cost1, cost2 <= 10^6
 * 链接：https://leetcode-cn.com/problems/number-of-ways-to-buy-pens-and-pencils
 */
public class Q2240 {
    public static void main(String[] args) {
        // 10
        System.out.println(new Q2240().waysToBuyPensPencils(10, 2, 5));
        // 3
        System.out.println(new Q2240().waysToBuyPensPencils(1, 1, 1));
        // 1
        System.out.println(new Q2240().waysToBuyPensPencils(5, 10, 10));
        // 9
        System.out.println(new Q2240().waysToBuyPensPencils(20, 10, 5));
    }

    public long waysToBuyPensPencils(int total, int cost1, int cost2) {
        long ret = 0;
        int n = total / cost1;
        for (int i = 0; i <= n; i++) {
            int remain = total - i * cost1;
            if (remain >= cost2) ret += remain / cost2;
            ret++;
        }
        return ret;
    }

}
