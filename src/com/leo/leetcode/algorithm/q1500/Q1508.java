package com.leo.leetcode.algorithm.q1500;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个数组 nums ，它包含 n 个正整数。你需要计算所有非空连续子数组的和，并将它们按升序排序，得到一个新的包含 n * (n + 1) / 2 个数字的数组。
 * 请你返回在新数组中下标为 left 到 right （下标从 1 开始）的所有数字和（包括左右端点）。由于答案可能很大，请你将它对 10^9 + 7 取模后返回。
 * 提示：
 * 1、1 <= nums.length <= 10^3
 * 2、nums.length == n
 * 3、1 <= nums[i] <= 100
 * 4、1 <= left <= right <= n * (n + 1) / 2
 * 链接：https://leetcode-cn.com/problems/range-sum-of-sorted-subarray-sums
 */
public class Q1508 {

    public static void main(String[] args) {
        // 13
        System.out.println(new Q1508().rangeSum(stringToIntegerArray("[1,2,3,4]"), 4, 1, 5));
        // 6
        System.out.println(new Q1508().rangeSum(stringToIntegerArray("[1,2,3,4]"), 4, 3, 4));
        // 50
        System.out.println(new Q1508().rangeSum(stringToIntegerArray("[1,2,3,4]"), 4, 1, 10));
    }

    public int rangeSum(int[] nums, int n, int left, int right) {
        final int MODULO = 1000000007;
        int sumsLength = n * (n + 1) / 2;
        int[] sums = new int[sumsLength];
        int index = 0;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums[j];
                sums[index++] = sum;
            }
        }
        Arrays.sort(sums);
        int ans = 0;
        for (int i = left - 1; i < right; i++) {
            ans = (ans + sums[i]) % MODULO;
        }
        return ans;
    }
}
