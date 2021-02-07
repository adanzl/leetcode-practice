package com.leo.leetcode.algorithm.q0600;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个长度为  n  的整数数组，请你判断在 最多 改变  1 个元素的情况下，该数组能否变成一个非递减数列。
 * 我们是这样定义一个非递减数列的：  对于数组中所有的  i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
 * <p>
 * 说明：
 * 1、1 <= n <= 10 ^ 4
 * 2、- 10 ^ 5 <= nums[i] <= 10 ^ 5
 * <p>
 * 链接：https://leetcode-cn.com/problems/non-decreasing-array
 */
public class Q665 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q665().checkPossibility(stringToIntegerArray("[5,7,1,8]")));
        // false
        System.out.println(new Q665().checkPossibility(stringToIntegerArray("[3,4,2,3]")));
        // false
        System.out.println(new Q665().checkPossibility(stringToIntegerArray("[4,2,1]")));
        // true
        System.out.println(new Q665().checkPossibility(stringToIntegerArray("[4,2,3]")));
    }


    public boolean checkPossibility(int[] nums) {
        int count = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] > nums[i]) {
                count++;
                if (count > 1) return false;
                if (i >= 2 && nums[i - 2] > nums[i]) nums[i] = nums[i - 1];
                else nums[i - 1] = nums[i];
            }
        }

        return true;
    }
}
