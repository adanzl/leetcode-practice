package com.leo.leetcode.algorithm.q2200;

import java.util.Arrays;
import java.util.Comparator;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个二维整数数组 stockPrices ，其中 stockPrices[i] = [ day_i, price_i] 表示股票在  day_i 的价格为 price_i 。
 * 折线图 是一个二维平面上的若干个点组成的图，横坐标表示日期，纵坐标表示价格，折线图由相邻的点连接而成。比方说下图是一个例子：
 * 请你返回要表示一个折线图所需要的 最少线段数 。
 * 提示：
 * 1、1 <= stockPrices.length <= 10^5
 * 2、stockPrices[i].length == 2
 * 3、1 <=  day_i, price_i <= 10^9
 * 4、所有  day_i 互不相同 。
 * 链接：https://leetcode.cn/problems/minimum-lines-to-represent-a-line-chart
 */
public class Q2280 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2280().minimumLines(stringToInt2dArray("[[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]")));
        // 1
        System.out.println(new Q2280().minimumLines(stringToInt2dArray("[[3,4],[1,2],[7,8],[2,3]]")));
        // 3
        System.out.println(new Q2280().minimumLines(stringToInt2dArray("[[1,1],[499999999,2],[999999998,3],[1000000000,5]]")));
    }

    public int minimumLines(int[][] stockPrices) {
        Arrays.sort(stockPrices, Comparator.comparingInt(o -> o[0]));
        int n = stockPrices.length, res = 1;
        if (n == 1) return 0;
        for (int i = 2; i < n; i++) {
            int x1 = stockPrices[i][0] - stockPrices[i - 1][0], y1 = stockPrices[i][1] - stockPrices[i - 1][1];
            int x2 = stockPrices[i - 1][0] - stockPrices[i - 2][0], y2 = stockPrices[i - 1][1] - stockPrices[i - 2][1];
            if (x1 * y2 != y1 * x2) res++;
        }
        return res;
    }

}
