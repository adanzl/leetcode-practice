package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且全部数字和（3 * k 项）最大的子数组，并返回这三个子数组。
 * 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。
 * 提示：
 * 1、1 <= nums.length <= 2 * 10^4
 * 2、1 <= nums[i] < 2^16
 * 3、1 <= k <= floor(nums.length / 3)
 * 链接：https://leetcode.cn/problems/maximum-sum-of-3-non-overlapping-subarrays
 */
public class Q689 {

    public static void main(String[] args) {
        // [0]
        System.out.println(Arrays.toString(new Q689().maxSumOfThreeSubarrays(stringToIntegerArray("[4,3,2,1]"), 1)));
        // [0,2,4]
        System.out.println(Arrays.toString(new Q689().maxSumOfThreeSubarrays(stringToIntegerArray("[1,2,1,2,1,2,1,2,1]"), 2)));
        // [0,3,5]
        System.out.println(Arrays.toString(new Q689().maxSumOfThreeSubarrays(stringToIntegerArray("[1,2,1,2,6,7,5,1]"), 2)));
    }

    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        int[][] dp3 = new int[n][3], dp1 = new int[n][1], dp2 = new int[n][2];
        long[] preSum = new long[n + 1], sum1 = new long[n], sum2 = new long[n], sum3 = new long[n];
        sum1[0] = nums[0];
        for (int i = 0; i < n; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
            long d = 0;
            if (i >= k - 1) {
                d = preSum[i + 1] - preSum[i - k + 1];
                if (i == 0 || d > sum1[i - 1]) {
                    sum1[i] = d;
                    dp1[i][0] = i - k + 1;
                } else {
                    sum1[i] = sum1[i - 1];
                    dp1[i] = dp1[i - 1];
                }
            }
            if (i >= k * 2 - 1) {
                long v = d + sum1[i - k];
                if (v > sum2[i - 1]) {
                    sum2[i] = v;
                    dp2[i][0] = dp1[i - k][0];
                    dp2[i][1] = i - k + 1;
                } else {
                    sum2[i] = sum2[i - 1];
                    dp2[i] = dp2[i - 1];
                }
            }
            if (i >= k * 3 - 1) {
                long v = d + sum2[i - k];
                if (v > sum3[i - 1]) {
                    sum3[i] = v;
                    dp3[i][0] = dp2[i - k][0];
                    dp3[i][1] = dp2[i - k][1];
                    dp3[i][2] = i - k + 1;
                } else {
                    sum3[i] = sum3[i - 1];
                    dp3[i] = dp3[i - 1];
                }
            }
        }
        return dp3[n - 1];
    }
}
