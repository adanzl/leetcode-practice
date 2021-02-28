package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
 *
 * 实现 NumArray 类：
 * 1、NumArray(int[] nums) 使用数组 nums 初始化对象
 * 2、int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
 *
 * 提示：
 * 1、0 <= nums.length <= 10^4
 * 2、-10^5 <= nums[i] <= 10^5
 * 3、0 <= i <= j < nums.length
 * 4、最多调用 10^4 次 sumRange 方法
 *
 * 链接：https://leetcode-cn.com/problems/range-sum-query-immutable
 */
public class Q303 {

    public static void main(String[] args) {
        NumArray obj;
        obj = new NumArray(stringToIntegerArray("[-2, 0, 3, -5, 2, -1]"));
        // 1
        System.out.println(obj.sumRange(0, 2));
        // -1
        System.out.println(obj.sumRange(2, 5));
        // -3
        System.out.println(obj.sumRange(0, 5));
    }

    static class NumArray {

        int[] sum;

        public NumArray(int[] nums) {
            sum = new int[nums.length];
            if (nums.length == 0) return;
            sum[0] = nums[0];
            for (int i = 1; i < nums.length; i++) sum[i] = nums[i] + sum[i - 1];
        }

        public int sumRange(int i, int j) {
            return sum[j] - (i == 0 ? 0 : sum[i - 1]);
        }
    }
}
