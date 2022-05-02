package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始长度为 n 的整数数组 nums 。
 * 下标 i 处的 平均差 指的是 nums 中 前 i + 1 个元素平均值和 后 n - i - 1 个元素平均值的 绝对差 。两个平均值都需要 向下取整 到最近的整数。
 * 请你返回产生 最小平均差 的下标。如果有多个下标最小平均差相等，请你返回 最小 的一个下标。
 * 注意：
 * 1、两个数的 绝对差 是两者差的绝对值。
 * 2、n 个元素的平均值是 n 个元素之 和 除以（整数除法） n 。
 * 3、0 个元素的平均值视为 0 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^5
 * 链接：https://leetcode-cn.com/problems/minimum-average-difference
 */
public class Q2256 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2256().minimumAverageDifference(stringToIntegerArray("[2,5,3,9,5,3]")));
        // 0
        System.out.println(new Q2256().minimumAverageDifference(stringToIntegerArray("[0]")));
    }

    public int minimumAverageDifference(int[] nums) {
        int n = nums.length, ret = 0;
        long min = Integer.MAX_VALUE;
        long[] preSum = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }
        for (int i = 0; i < n - 1; i++) {
            long v = Math.abs(preSum[i + 1] / (i + 1) - (preSum[n] - preSum[i + 1]) / (n - i - 1));
            if (v < min) {
                min = v;
                ret = i;
            }
        }
        if (preSum[n] / n < min) ret = n - 1;
        return ret;
    }
}
