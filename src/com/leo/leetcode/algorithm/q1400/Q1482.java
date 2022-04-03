package com.leo.leetcode.algorithm.q1400;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 bloomDay，以及两个整数 m 和 k 。
 * 现需要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。
 * 花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 时盛开，恰好 可以用于 一束 花中。
 * 请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。
 * 提示：
 * 1、bloomDay.length == n
 * 2、1 <= n <= 10^5
 * 3、1 <= bloomDay[i] <= 10^9
 * 4、1 <= m <= 10^6
 * 5、1 <= k <= n
 * 链接：https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets
 */
public class Q1482 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1482().minDays(stringToIntegerArray("[1,10,3,10,2]"), 3, 1));
        // -1
        System.out.println(new Q1482().minDays(stringToIntegerArray("[1,10,3,10,2]"), 3, 2));
        // 12
        System.out.println(new Q1482().minDays(stringToIntegerArray("[7,7,7,7,12,7,7]"), 2, 3));
        // 1000000000
        System.out.println(new Q1482().minDays(stringToIntegerArray("[1000000000,1000000000]"), 1, 1));
        // 9
        System.out.println(new Q1482().minDays(stringToIntegerArray("[1,10,2,9,3,8,4,7,5,6]"), 4, 2));
    }

    public int minDays(int[] bloomDay, int m, int k) {
        int ret = -1, l = 1, r = 1_000_000_000;
        while (l <= r) {
            int mid = l + ((r - l) >> 1), count = 0, len = 0;
            for (int bDay : bloomDay) {
                if (bDay <= mid) len++;
                else len = 0;
                if (len >= k) {
                    count++;
                    len -= k;
                }
            }
            if (count >= m) {
                ret = mid;
                r = mid - 1;
            } else l = mid + 1;
        }
        return ret;
    }
}
