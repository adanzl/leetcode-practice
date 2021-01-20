package com.leo.leetcode.algorithm.q0600;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.Arrays;

/**
 * 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
 * 注意:
 * 1、给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
 * 2、输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
 * <p>
 * 链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers
 */
public class Q628 {

    public static void main(String[] args) {
        // -6
        System.out.println(new Q628().maximumProduct(stringToIntegerArray("[-1,-2,-3,-4]")));
        // 6
        System.out.println(new Q628().maximumProduct(stringToIntegerArray("[1,2,3]")));
        // 24
        System.out.println(new Q628().maximumProduct(stringToIntegerArray("[1,2,3,4]")));
        // 24
        System.out.println(new Q628().maximumProduct(stringToIntegerArray("[1,2,-3,-4]")));
        // 8
        System.out.println(new Q628().maximumProduct(stringToIntegerArray("[-1,-2,3,4]")));
        // 24
        System.out.println(new Q628().maximumProduct(stringToIntegerArray("[-1,-2,-3,4]")));
    }

    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        if (nums[1] > 0) return nums[nums.length - 1] * nums[nums.length - 2] * nums[nums.length - 3];
        return Math.max(nums[0] * nums[1] * nums[nums.length - 1], nums[nums.length - 2] * nums[nums.length - 3] * nums[nums.length - 1]);
    }
}
