package com.leo.leetcode.algorithm.q0400;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
 * 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
 * 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
 * 子数组 是数组中的一个连续序列。
 * 提示：
 * 1、1 <= nums.length <= 5000
 * 2、-1000 <= nums[i] <= 1000
 * 链接：https://leetcode-cn.com/problems/arithmetic-slices
 */
public class Q413 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q413().numberOfArithmeticSlices(stringToIntegerArray("[1,1,1,1]")));
        // 6
        System.out.println(new Q413().numberOfArithmeticSlices(stringToIntegerArray("[1,1,1,1,1]")));
        // 6
        System.out.println(new Q413().numberOfArithmeticSlices(stringToIntegerArray("[1,2,3,4,6,8,10]")));
        // 3
        System.out.println(new Q413().numberOfArithmeticSlices(stringToIntegerArray("[1,2,3,4]")));
        // 0
        System.out.println(new Q413().numberOfArithmeticSlices(stringToIntegerArray("[1]")));
    }

    public int numberOfArithmeticSlices(int[] nums) {
        if (nums.length < 3) return 0;
        int ret = 0, d0 = nums[1] - nums[0], len = 1;
        for (int i = 2; i < nums.length; i++) {
            int d1 = nums[i] - nums[i - 1];
            if (d1 != d0) {
                d0 = d1;
                len = 1;
            } else {
                ret += len++;
            }
        }
        return ret;
    }
}
