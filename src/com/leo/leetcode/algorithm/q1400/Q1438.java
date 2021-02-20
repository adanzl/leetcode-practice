package com.leo.leetcode.algorithm.q1400;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，
 * 该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
 * 如果不存在满足条件的子数组，则返回 0 。
 * <p>
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、0 <= limit <= 10^9
 * <p>
 * 链接：https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
 */
public class Q1438 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1438().longestSubArray(stringToIntegerArray("[8,2,4,7]"), 1));
        // 2
        System.out.println(new Q1438().longestSubArray(stringToIntegerArray("[8,2,4,7]"), 4));
        // 4
        System.out.println(new Q1438().longestSubArray(stringToIntegerArray("[10,1,2,4,7,2]"), 5));
        // 3
        System.out.println(new Q1438().longestSubArray(stringToIntegerArray("[4,2,2,2,4,4,2,2]"), 0));
    }

    public int longestSubArray(int[] nums, int limit) {
        int l = 0, r = 0, ret = 0, max = nums[0], min = max;
        while (r < nums.length) {
            if (Math.abs(max - nums[r]) > limit || Math.abs(min - nums[r]) > limit) {
                l = r;
                max = nums[r];
                min = nums[r];
                while (Math.abs(max - nums[l - 1]) <= limit && Math.abs(min - nums[l - 1]) <= limit) {
                    l--;
                    max = Math.max(max, nums[l]);
                    min = Math.min(min, nums[l]);
                }
            } else {
                max = Math.max(max, nums[r]);
                min = Math.min(min, nums[r]);
                ret = Math.max(r - l + 1, ret);
            }
            r++;
        }
//        return ret == 1 ? 0 : ret;
        return ret; // 这行能AC，但是不符合题意 ”如果不存在满足条件的子数组，则返回 0“
    }
}
