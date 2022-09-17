package com.leo.leetcode.algorithm.q0900;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.Arrays;

/**
 * 给你一个整数数组 nums，和一个整数 k 。
 * 对于每个下标 i（0 <= i < nums.length），将 nums[i] 变成 nums[i] + k 或 nums[i] - k 。
 * nums 的 分数 是 nums 中最大元素和最小元素的差值。
 * 在更改每个下标对应的值之后，返回 nums 的最小 分数 。
 * 提示：
 * 1、1 <= nums.length <= 10^4
 * 2、0 <= nums[i] <= 10^4
 * 3、0 <= k <= 10^4
 * 链接：https://leetcode-cn.com/problems/smallest-range-ii
 */
public class Q910 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q910().smallestRangeII(stringToIntegerArray("[1]"), 0));
        // 6
        System.out.println(new Q910().smallestRangeII(stringToIntegerArray("[0,10]"), 2));
        // 3
        System.out.println(new Q910().smallestRangeII(stringToIntegerArray("[1,3,6]"), 3));
        //
        System.out.println(new Q910().smallestRangeII(stringToIntegerArray("[1]"), 0));
    }

    public int smallestRangeII(int[] nums, int k) {
        Arrays.sort(nums);
        int ret = nums[nums.length - 1] - nums[0];
        for (int i = 0; i < nums.length - 1; i++) {
            int h = Math.max(nums[nums.length - 1] - k, nums[i] + k);
            int l = Math.min(nums[0] + k, nums[i + 1] - k);
            ret = Math.min(ret, h - l);
        }
        return ret;
    }
}
