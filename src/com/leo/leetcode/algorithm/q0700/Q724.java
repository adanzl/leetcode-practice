package com.leo.leetcode.algorithm.q0700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。
 * 我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
 * 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
 * <p>
 * 说明：
 * 1、nums 的长度范围为 [0, 10000]。
 * 2、任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。
 * <p>
 * 链接：https://leetcode-cn.com/problems/find-pivot-index
 */
public class Q724 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q724().pivotIndex(stringToIntegerArray("[1, 7, 3, 6, 5, 6]")));
        // -1
        System.out.println(new Q724().pivotIndex(stringToIntegerArray("[1, 2, 3]")));
    }

    public int pivotIndex(int[] nums) {
        int total = 0, sum = 0;
        for (int v : nums) total += v;
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i];
            if (sum * 2 + v == total) return i;
            sum += v;
        }
        return -1;
    }
}
