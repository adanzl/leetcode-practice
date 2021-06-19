package com.leo.leetcode.algorithm.q0500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
 * 说明 :
 * 1、数组的长度为 [1, 20,000]。
 * 2、数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
 * <p>
 * 链接：https://leetcode-cn.com/problems/subarray-sum-equals-k/
 */
public class Q560 {
    public static void main(String[] args) {
        System.out.println(new Q560().subArraySum(stringToIntegerArray("[-1,-1,1]"), 0)); // 1
        System.out.println(new Q560().subArraySum(stringToIntegerArray("[1,2,3]"), 3)); // 2
        System.out.println(new Q560().subArraySum(stringToIntegerArray("[1,1,1]"), 0)); // 0
        System.out.println(new Q560().subArraySum(stringToIntegerArray("[1,1,1]"), 2)); // 2
        System.out.println(new Q560().subArraySum(stringToIntegerArray("[1]"), 2)); // 0
    }

    // sum(i,j) = sum(0,j) - sum(0,i) + nums[i]
    // sum[i] = sum[i-1] + nums[i];
    public int subArraySum(int[] nums, int k) {
        int out = 0;
        int[] sum = new int[nums.length + 1];
        for (int i = 1; i < sum.length; i++)
            sum[i] = sum[i - 1] + nums[i - 1];
        for (int i = 0; i < sum.length; i++) {
            for (int j = 0; j < i; j++) {
                if (sum[i] - sum[j] == k)
                    out++;
            }
        }
        return out;
    }
}
