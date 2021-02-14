package com.leo.leetcode.algorithm.q0400;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个二进制数组， 计算其中最大连续1的个数。
 * <p>
 * 注意：
 * 1、输入的数组只包含 0 和1。
 * 2、输入数组的长度是正整数，且不超过 10,000。
 * <p>
 * 链接：https://leetcode-cn.com/problems/max-consecutive-ones/
 */
public class Q485 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q485().findMaxConsecutiveOnes(stringToIntegerArray("[0,1,1,1,1,0,1,1,1]")));
        // 4
        System.out.println(new Q485().findMaxConsecutiveOnes(stringToIntegerArray("[1,1,1,1,0,1,1,1]")));
        // 3
        System.out.println(new Q485().findMaxConsecutiveOnes(stringToIntegerArray("[1,1,1,0,1,1,1]")));
        // 3
        System.out.println(new Q485().findMaxConsecutiveOnes(stringToIntegerArray("[1,1,0,1,1,1]")));
    }

    public int findMaxConsecutiveOnes(int[] nums) {
        int ret = 0, l = -1, r = 0;
        while (r < nums.length) {
            if (nums[r] != 1) l = r;
            ret = Math.max(ret, r - l);
            r++;
        }
        return Math.max(ret, r - l - 1);
    }
}
