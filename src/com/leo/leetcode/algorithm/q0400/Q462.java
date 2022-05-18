package com.leo.leetcode.algorithm.q0400;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。
 * 在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= nums.length <= 10^5
 * 3、-10^9 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/
 */
public class Q462 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q462().minMoves2(stringToIntegerArray("[1,2,3]")));
        // 16
        System.out.println(new Q462().minMoves2(stringToIntegerArray("[1,10,2,9]")));
    }

    public int minMoves2(int[] nums) {
        int ret = 0, n = nums.length;
        long mid;
        Arrays.sort(nums);
        if ((n & 1) == 1) mid = nums[n / 2] / 2;
        else mid = (nums[n / 2] + nums[n / 2 - 1]) / 2;
        for (int num : nums) ret += Math.abs(num - mid);
        return ret;
    }
}
