package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums 。一次操作中，选择 任意 非负整数 x 和一个下标 i ，更新 nums[i] 为 nums[i] AND (nums[i] XOR x) 。
 * 注意，AND 是逐位与运算，XOR 是逐位异或运算。
 * 请你执行 任意次 更新操作，并返回 nums 中所有元素 最大 逐位异或和。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^8
 * 链接：https://leetcode.cn/problems/maximum-xor-after-operations
 */
public class Q2317 {

    public static void main(String[] args) {
        // 7
        System.out.println(new Q2317().maximumXOR(stringToIntegerArray("[3,2,4,6]")));
        // 11
        System.out.println(new Q2317().maximumXOR(stringToIntegerArray("[1,2,3,9,2]")));
    }

    public int maximumXOR(int[] nums) {
        int ret = 0;
        for (int num : nums) ret |= num;
        return ret;
    }
}
