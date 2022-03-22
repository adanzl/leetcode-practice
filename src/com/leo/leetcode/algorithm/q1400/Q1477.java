package com.leo.leetcode.algorithm.q1400;

/**
 * 给你一个整数数组 arr 和一个整数值 target 。
 * 请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。
 * 请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。
 * 链接：https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum
 */
public class Q1477 {

    public static void main(String[] args) {
        System.out.println(new Q1477().minSumOfLengths(new int[]{24, 1, 21, 1, 4, 3, 27, 7, 5, 1, 12, 1, 1, 43, 2, 5, 4, 54, 34}, 54)); // 5
        System.out.println(new Q1477().minSumOfLengths(new int[]{31, 1, 1, 18, 15, 3, 15, 14}, 33)); // 5
        System.out.println(new Q1477().minSumOfLengths(new int[]{47, 17, 4, 8, 8, 2, 1, 1, 8, 35, 30, 1, 11, 1, 1, 1, 44, 1, 3, 27, 2, 8}, 88)); // 16
        System.out.println(new Q1477().minSumOfLengths(new int[]{7, 3, 4, 7}, 7)); // 2
        System.out.println(new Q1477().minSumOfLengths(new int[]{1, 6, 1}, 7)); // -1
        System.out.println(new Q1477().minSumOfLengths(new int[]{4, 3, 2, 6, 2, 3, 4}, 6)); // -1
        System.out.println(new Q1477().minSumOfLengths(new int[]{3, 1, 1, 1, 5, 1, 2, 1}, 3)); // 3
        System.out.println(new Q1477().minSumOfLengths(new int[]{3, 2, 2, 4, 3}, 3)); // 2
        System.out.println(new Q1477().minSumOfLengths(new int[]{5, 5, 4, 4, 5}, 3)); // -1
    }

    public int minSumOfLengths(int[] arr, int target) {
        final int MAX = 1000000;
        int t = arr[0], limit = 1, out = MAX;
        int[] lMark = new int[arr.length], rMark = new int[arr.length];
        lMark[0] = MAX;
        for (int i = 0; i < arr.length; ) {
            if (t >= target) {
                if (t == target) lMark[limit - 1] = limit == 1 ? limit - i : Math.min(lMark[limit - 2], limit - i);
                else lMark[limit - 1] = limit == 1 ? MAX : lMark[limit - 1 - 1];
                t -= arr[i];
                i++;
            } else {
                if (limit == arr.length) break;
                t += arr[limit];
                lMark[limit] = lMark[limit - 1];
                limit++;
            }
        }
        t = arr[arr.length - 1];
        limit = arr.length - 2;
        rMark[arr.length - 1] = MAX;
        for (int i = arr.length - 1; i >= 0; ) {
            if (t >= target) {
                if (t == target)
                    rMark[limit + 1] = limit == arr.length - 2 ? i - limit : Math.min(rMark[limit + 2], i - limit);
                else rMark[limit + 1] = limit == arr.length - 2 ? MAX : rMark[limit + 2];
                t -= arr[i];
                i--;
            } else {
                if (limit == -1) break;
                t += arr[limit];
                rMark[limit] = rMark[limit + 1];
                limit--;
            }
        }
        for (int i = 0; i < arr.length - 1; i++) out = Math.min(out, lMark[i] + rMark[i + 1]);
        return out == MAX ? -1 : out;
    }
}
