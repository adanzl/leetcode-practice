package com.leo.leetcode.algorithm.q2200;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * Alice 是 n 个花园的园丁，她想通过种花，最大化她所有花园的总美丽值。
 * 给你一个下标从 0 开始大小为 n 的整数数组 flowers ，其中 flowers[i] 是第 i 个花园里已经种的花的数目。已经种了的花 不能 移走。
 * 同时给你 newFlowers ，表示 Alice 额外可以种花的 最大数目 。同时给你的还有整数 target ，full 和 partial 。
 * 如果一个花园有 至少 target 朵花，那么这个花园称为 完善的 ，花园的 总美丽值 为以下分数之 和 ：
 * 完善 花园数目乘以 full.
 * 剩余 不完善 花园里，花的 最少数目 乘以 partial 。如果没有不完善花园，那么这一部分的值为 0 。
 * 请你返回 Alice 种最多 newFlowers 朵花以后，能得到的 最大 总美丽值。
 * 提示：
 * 1、1 <= flowers.length <= 10^5
 * 2、1 <= flowers[i], target <= 10^5
 * 3、1 <= newFlowers <= 10^10
 * 4、1 <= full, partial <= 10^5
 * 链接：https://leetcode-cn.com/problems/maximum-total-beauty-of-the-gardens/
 */
public class Q2234 {
    public static void main(String[] args) {
        // 14
        System.out.println(new Q2234().maximumBeauty(stringToIntegerArray("[1,3,1,1]"), 7, 6, 12, 1));
        // 30
        System.out.println(new Q2234().maximumBeauty(stringToIntegerArray("[2,4,5,3]"), 10, 5, 2, 6));
        // 195
        System.out.println(new Q2234().maximumBeauty(stringToIntegerArray("[10,9,16,14,6,5,11,12,17,2,11,15,1]"), 80, 14, 15, 1));
        // 104
        System.out.println(new Q2234().maximumBeauty(stringToIntegerArray("[19,17,6,9,19]"), 24, 10, 17, 4));
        // 75
        System.out.println(new Q2234().maximumBeauty(stringToIntegerArray("[18,16,10,10,5]"), 10, 3, 15, 4));
        // 876237680
        System.out.println(new Q2234().maximumBeauty(stringToIntegerArray("[96580,4267,90191,30413,22764,34425,1516,28958,31972,86787,19923,4924,26293,76810,11446,24051,64071,95062,36623,73174,66453,64427,63194,36295,41187,83049,5856,74647,90816,82635,64161,72621,3241,12255,96849,54401,37420,59093,98981,38839,67817,93998,81727,93827,25785,33118,26416,84625,20879,77979,49471,54136,29011,72376,71453,73290,85941,67610,81908,9520,56404,69569,73932,61471,89486,77771,67395,11079,87888,80616,41589,12111,54593]")
                , 2322540, 100000, 49452, 10264));
    }

    public long maximumBeauty(int[] flowers, long newFlowers, int target, int full, int partial) {
        int n = flowers.length;
        long ret = 0, leftFlowers = newFlowers;
        Arrays.sort(flowers);
        if (flowers[0] >= target) return (long) n * full;
        for (int i = 0; i < n; i++) {
            flowers[i] = Math.min(flowers[i], target);
            leftFlowers -= target - flowers[i];
        }
        long min = target;
        for (int i = 0, p = n - 1; i <= n; i++) {
            long score = (long) i * full;
            while (leftFlowers < 0 && min > flowers[0]) {
                while (p >= 0 && flowers[p] >= min) p--;
                if (p < 0) break;
                min--;
                leftFlowers += 1 + p;
            }
            if (leftFlowers < 0) break;
            if (i < n) score += Math.min(min, target - 1) * partial;
            ret = Math.max(ret, score);
            if (i < n) leftFlowers -= target - Math.max(min, flowers[n - i - 1]);
            p = Math.min(p, n - i - 1 - 1);
        }
        return ret;
    }
}
