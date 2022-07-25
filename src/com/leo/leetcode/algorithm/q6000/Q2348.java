package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，返回全部为 0 的 子数组 数目。
 * 子数组 是一个数组中一段连续非空元素组成的序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^9 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/number-of-zero-filled-subarrays/
 */
public class Q2348 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q2348().zeroFilledSubarray(stringToIntegerArray("[1,3,0,0,2,0,0,4]")));
        // 9
        System.out.println(new Q2348().zeroFilledSubarray(stringToIntegerArray("[0,0,0,2,0,0]")));
        // 0
        System.out.println(new Q2348().zeroFilledSubarray(stringToIntegerArray("[2,10,2019]")));
    }

    public long zeroFilledSubarray(int[] nums) {
        long ret = 0;
        int count = 0;
        for (int num : nums) {
            if (num == 0) {
                count++;
            } else {
                ret += (1L + count) * count / 2;
                count = 0;
            }
        }
        ret += (1L + count) * count / 2;
        return ret;
    }
}
