package com.leo.leetcode.algorithm.q1100;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组 arr 和一个整数 k ，通过重复 k 次来修改数组。
 * 例如，如果 arr = [1, 2] ， k = 3 ，那么修改后的数组将是 [1, 2, 1, 2, 1, 2] 。
 * 返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 0，在这种情况下它的总和也是 0。
 * 由于 结果可能会很大，需要返回的 10^9 + 7 的 模 。
 * 提示：
 * 1、1 <= arr.length <= 10^5
 * 2、1 <= k <= 10^5
 * 3、-10^4 <= arr[i] <= 10^4
 * 链接：https://leetcode.cn/problems/k-concatenation-maximum-sum
 */
public class Q1191 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q1191().kConcatenationMaxSum(stringToIntegerArray("[2,-5,1,0,-2,-2,2]"), 2));
        // 1
        System.out.println(new Q1191().kConcatenationMaxSum(stringToIntegerArray("[1,-1]"), 1));
        // 2
        System.out.println(new Q1191().kConcatenationMaxSum(stringToIntegerArray("[1,-2,1]"), 5));
        // 9
        System.out.println(new Q1191().kConcatenationMaxSum(stringToIntegerArray("[1,2]"), 3));
        // 0
        System.out.println(new Q1191().kConcatenationMaxSum(stringToIntegerArray("[-1,-2]"), 7));
    }

    public int kConcatenationMaxSum(int[] arr, int k) {
        int n = arr.length, MOD = 1000000007;
        long[] sumLeft = new long[n + 1], sumRight = new long[n + 1];
        long maxLeft = Long.MIN_VALUE, maxRight = Long.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            sumLeft[i + 1] = sumLeft[i] + arr[i];
            maxLeft = Math.max(maxLeft, sumLeft[i + 1]);
            sumRight[i + 1] = sumRight[i] + arr[n - 1 - i];
            maxRight = Math.max(maxRight, sumRight[i + 1]);
        }
        long ret = maxSubArray(arr);
        if (k == 1) return (int) (ret % MOD);
        if (sumLeft[n] > 0) {
            long v = sumLeft[n] * (k - 2) + maxLeft + maxRight;
            ret = Math.max(ret, v);
        }
        ret = Math.max(ret, maxLeft + maxRight);
        ret = Math.max(0, ret);
        return (int) (ret % MOD);
    }

    // Kadane 求子数组最大和 https://hackernoon.com/kadanes-algorithm-explained-50316f4fd8a6
    long maxSubArray(int[] nums) {
        int n = nums.length;
        long[] dp = new long[n];
        dp[0] = nums[0];
        long ret = dp[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
            ret = Math.max(ret, dp[i]);
        }
        return ret;
    }
}
