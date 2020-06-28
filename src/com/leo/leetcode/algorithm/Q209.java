package com.leo.leetcode.algorithm;

/**
 * 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。
 * 如果不存在符合条件的连续子数组，返回 0。
 * 链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
 */
public class Q209 {
    public static void main(String[] args) {
        System.out.println(new Q209().minSubArrayLen(7, new int[]{2, 3, 1, 2, 4, 3})); // 2
        System.out.println(new Q209().minSubArrayLen(100, new int[]{1, 1, 1, 2, 4, 3})); // 0
    }

    public int minSubArrayLen(int s, int[] nums) {
        int l = 0, r = 0, sum = 0, out = Integer.MAX_VALUE;
        while (r < nums.length) {
            sum += nums[r];
            if (sum >= s) {
                while (sum - nums[l] >= s) sum -= nums[l++];
                out = Math.min(out, r - l + 1);
            }
            r++;
        }
        return out == Integer.MAX_VALUE ? 0 : out;
    }
}
