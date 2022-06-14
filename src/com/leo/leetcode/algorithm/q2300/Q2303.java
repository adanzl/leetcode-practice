package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个下标从 0 开始的二维整数数组 brackets ，其中 brackets[i] = [upper_i, percent_i] ，表示第 i 个税级的上限是 upper_i ，征收的税率为 percent_i 。
 * 税级按上限 从低到高排序（在满足 0 < i < brackets.length 的前提下，upper_i-1 < upper_i）。
 * 税款计算方式如下：
 * 1、不超过 upper0 的收入按税率 percent0 缴纳
 * 2、接着 upper1 - upper0 的部分按税率 percent1 缴纳
 * 3、然后 upper2 - upper1 的部分按税率 percent2 缴纳
 * 4、以此类推
 * 给你一个整数 income 表示你的总收入。返回你需要缴纳的税款总额。与标准答案误差不超 10-5 的结果将被视作正确答案。
 * 提示：
 * 1、1 <= brackets.length <= 100
 * 2、1 <= upper_i <= 1000
 * 3、0 <= percent_i <= 100
 * 4、0 <= income <= 1000
 * 5、upper_i 按递增顺序排列
 * 6、upper_i 中的所有值 互不相同
 * 7、最后一个税级的上限大于等于 income
 * 链接：https://leetcode.cn/problems/calculate-amount-paid-in-taxes
 */
public class Q2303 {

    public static void main(String[] args) {
        // 2.6500
        System.out.println(new Q2303().calculateTax(stringToInt2dArray("[[3,50],[7,10],[12,25]]"), 10));
        // 0.2500
        System.out.println(new Q2303().calculateTax(stringToInt2dArray("[[1,0],[4,25],[5,50]]"), 2));
        // 0.0000
        System.out.println(new Q2303().calculateTax(stringToInt2dArray("[[2,50]]"), 0));
    }

    public double calculateTax(int[][] brackets, int income) {
        double ret = 0, pre = 0;
        for (int i = 0; i < brackets.length && income > pre; i++) {
            double v = Math.min(brackets[i][0], income) - pre;
            ret += v * brackets[i][1] / 100.0;
            pre = brackets[i][0];
        }
        return ret;
    }
}
