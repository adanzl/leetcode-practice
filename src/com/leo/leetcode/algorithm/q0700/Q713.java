package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个正整数数组 nums和整数 k 。
 * 请找出该数组内乘积小于 k 的连续的子数组的个数。
 * 提示:
 * 1、1 <= nums.length <= 3 * 10^4
 * 2、1 <= nums[i] <= 1000
 * 3、0 <= k <= 10^6
 * 链接：https://leetcode-cn.com/problems/subarray-product-less-than-k/
 */
public class Q713 {
    public static void main(String[] args) {
        // 1
        System.out.println(new Q713().numSubArrayProductLessThanK(stringToIntegerArray("[1,2,3]"), 2));
        // 0
        System.out.println(new Q713().numSubArrayProductLessThanK(stringToIntegerArray("[1,2,3]"), 0));
        // 6
        System.out.println(new Q713().numSubArrayProductLessThanK(stringToIntegerArray("[1,1,1,3]"), 2));
        // 8
        System.out.println(new Q713().numSubArrayProductLessThanK(stringToIntegerArray("[10,5,2,6]"), 100));
    }

    public int numSubArrayProductLessThanK(int[] nums, int k) {
        int ret = 0, l = 0, r = 0, multi = 1, len = nums.length;
        while (l < len) {
            while (r < len && multi * nums[r] < k) multi *= nums[r++];
            ret += r - l;
            if (l != r) multi /= nums[l];
            l++;
            r = Math.max(r, l);
        }
        return ret;
    }
}
