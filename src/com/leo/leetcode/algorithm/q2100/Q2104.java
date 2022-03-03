package com.leo.leetcode.algorithm.q2100;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
 * 返回 nums 中 所有 子数组范围的 和 。
 * 子数组是数组中一个连续 非空 的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、-10^9 <= nums[i] <= 10^9
 * 进阶：你可以设计一种时间复杂度为 O(n) 的解决方案吗？
 * 链接：https://leetcode-cn.com/problems/sum-of-subarray-ranges
 */
public class Q2104 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q2104().subArrayRanges(stringToIntegerArray("[1,2,3]")));
        // 4
        System.out.println(new Q2104().subArrayRanges(stringToIntegerArray("[1,3,3]")));
        // 59
        System.out.println(new Q2104().subArrayRanges(stringToIntegerArray("[4,-2,-3,4,1]")));
    }

    public long subArrayRanges(int[] nums) {
        long ret = 0;
        for (int i = 0; i < nums.length; i++) {
            int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
            for (int j = i; j < nums.length; j++) {
                min = Math.min(min, nums[j]);
                max = Math.max(max, nums[j]);
                ret += max - min;
            }
        }
        return ret;
    }
}
