package com.leo.leetcode.algorithm.q2300;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你两个整数 m 和 n ，分别表示一块矩形木块的高和宽。
 * 同时给你一个二维整数数组 prices ，其中 prices[i] = [hi, wi, price_i] 表示你可以以 price_i 元的价格卖一块高为 hi 宽为 wi 的矩形木块。
 * 每一次操作中，你必须按下述方式之一执行切割操作，以得到两块更小的矩形木块：
 * 沿垂直方向按高度 完全 切割木块，或 沿水平方向按宽度 完全 切割木块
 * 在将一块木块切成若干小木块后，你可以根据 prices 卖木块。你可以卖多块同样尺寸的木块。你不需要将所有小木块都卖出去。你 不能 旋转切好后木块的高和宽。
 * 请你返回切割一块大小为 m x n 的木块后，能得到的 最多 钱数。
 * 注意你可以切割木块任意次。
 * 提示：
 * 1、1 <= m, n <= 200
 * 2、1 <= prices.length <= 2 * 10^4
 * 3、prices[i].length == 3
 * 4、1 <= hi <= m
 * 5、1 <= wi <= n
 * 6、1 <= price_i <= 10^6
 * 7、所有 (hi, wi) 互不相同 。
 * 链接：https://leetcode.cn/problems/selling-pieces-of-wood
 */
public class Q2312 {

    public static void main(String[] args) {
        // 22
        System.out.println(new Q2312().sellingWood(3, 5, stringToInt2dArray("[[1,4,2],[2,2,7],[1,1,1]]")));
        // 19
        System.out.println(new Q2312().sellingWood(3, 5, stringToInt2dArray("[[1,4,2],[2,2,7],[2,1,3]]")));
        // 32
        System.out.println(new Q2312().sellingWood(4, 6, stringToInt2dArray("[[3,2,10],[1,4,2],[4,1,3]]")));
    }

    public long sellingWood(int m, int n, int[][] prices) {
        long[][] cnt = new long[m + 1][n + 1];
        int[][] p = new int[m + 1][n + 1];
        for (int[] price : prices) {
            int h = price[0];
            int w = price[1];
            p[h][w] = price[2];
        }
        for (int i = 1; i <= m; i++) {
            Arrays.fill(cnt[i], -1);
            cnt[i][0] = 0;
        }
        return func(cnt, m, n, p);
    }

    long func(long[][] cnt, int m, int n, int[][] p) {
        if (cnt[m][n] != -1) return cnt[m][n];
        for (int i = 1; i < m; i++) cnt[m][n] = Math.max(cnt[m][n], func(cnt, i, n, p) + func(cnt, m - i, n, p));
        for (int i = 1; i < n; i++) cnt[m][n] = Math.max(cnt[m][n], func(cnt, m, i, p) + func(cnt, m, n - i, p));
        cnt[m][n] = Math.max(cnt[m][n], p[m][n]);
        return cnt[m][n];
    }
}
