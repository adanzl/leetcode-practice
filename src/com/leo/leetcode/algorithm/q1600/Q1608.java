package com.leo.leetcode.algorithm.q1600;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个非负整数数组 nums 。如果存在一个数 x ，使得 nums 中恰好有 x 个元素 大于或者等于 x ，那么就称 nums 是一个 特殊数组 ，而 x 是该数组的 特征值 。
 * 注意： x 不必 是 nums 的中的元素。
 * 如果数组 nums 是一个 特殊数组 ，请返回它的特征值 x 。否则，返回 -1 。可以证明的是，如果 nums 是特殊数组，那么其特征值 x 是 唯一的 。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、0 <= nums[i] <= 1000
 * 链接：https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x
 */
public class Q1608 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1608().specialArray(stringToIntegerArray("[3,5]")));
        // -1
        System.out.println(new Q1608().specialArray(stringToIntegerArray("[0,0]")));
        // 3
        System.out.println(new Q1608().specialArray(stringToIntegerArray("[0,4,3,0,4]")));
        // -1
        System.out.println(new Q1608().specialArray(stringToIntegerArray("[2,2,2,0,4]")));
        // -1
        System.out.println(new Q1608().specialArray(stringToIntegerArray("[3,6,7,7,0]")));
    }

    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = 1; i <= n; i++) {
            if (nums[n - i] >= i && (i == n || nums[n - i - 1] < i)) return i;
        }
        return -1;
    }
}
