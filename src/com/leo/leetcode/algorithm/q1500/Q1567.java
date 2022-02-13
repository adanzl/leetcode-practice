package com.leo.leetcode.algorithm.q1500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。
 * 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
 * 请你返回乘积为正数的最长子数组长度。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^9 <= nums[i] <= 10^9
 * 链接：https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product
 */
public class Q1567 {

    public static void main(String[] args) {
        // 8
        System.out.println(new Q1567().getMaxLen(stringToIntegerArray("[5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]")));
        // 4
        System.out.println(new Q1567().getMaxLen(stringToIntegerArray("[1,2,3,5,-6,4,0,10]")));
        // 3
        System.out.println(new Q1567().getMaxLen(stringToIntegerArray("[0,1,-2,-3,-4]")));
        // 4
        System.out.println(new Q1567().getMaxLen(stringToIntegerArray("[1,-2,-3,4]")));
        // 1
        System.out.println(new Q1567().getMaxLen(stringToIntegerArray("[-1,2]")));
        // 2
        System.out.println(new Q1567().getMaxLen(stringToIntegerArray("[-1,-2,-3,0,1]")));
    }

    public int getMaxLen(int[] nums) {
        int ret = 0, p1 = -1, p2 = 0, nc = 0, pre_i = -1;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (num < 0) {
                if (p1 == -1) p1 = i;
                p2 = i;
                ++nc;
            }
            if (num == 0) {
                if ((nc & 1) == 0) {
                    ret = Math.max(ret, i - pre_i - 1);
                } else {
                    ret = Math.max(ret, p2 - pre_i - 1);
                    ret = Math.max(ret, i - 1 - p1);
                }
                nc = 0;
                pre_i = i;
                p1 = -1;
            }
        }
        if ((nc & 1) == 0) {
            ret = Math.max(ret, nums.length - pre_i - 1);
        } else {
            ret = Math.max(ret, nums.length - 1 - p1);
            ret = Math.max(ret, p2 - pre_i - 1);
        }
        return ret;
    }
}
