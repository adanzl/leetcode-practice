package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，它包含 2 * n 个整数。
 * 你需要将 nums 划分成 n 个数对，满足：
 * 每个元素 只属于一个 数对。
 * 同一数对中的元素 相等 。
 * 如果可以将 nums 划分成 n 个数对，请你返回 true ，否则返回 false 。
 * 提示：
 * 1、nums.length == 2 * n
 * 2、1 <= n <= 500
 * 3、1 <= nums[i] <= 500
 * 链接：https://leetcode-cn.com/problems/divide-array-into-equal-pairs
 */
public class Q2206 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q2206().divideArray(stringToIntegerArray("[3,2,3,2,2,2]")));
        // false
        System.out.println(new Q2206().divideArray(stringToIntegerArray("[1,2,3,4]")));
    }

    public boolean divideArray(int[] nums) {
        int[] map = new int[501];
        for (int n : nums) {
            map[n]++;
        }
        for (int n : map) {
            if ((n & 1) != 0) return false;
        }
        return true;
    }
}
