package com.leo.leetcode.algorithm.q0000;

import java.util.Arrays;

/**
 * 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
 * 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
 * 必须原地修改，只允许使用额外常数空间。
 * 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 * 链接：https://leetcode-cn.com/problems/next-permutation
 */
public class Q31 {
    public static void main(String[] args) {
        int[] nums = new int[]{1, 2, 3};
        new Q31().nextPermutation(nums);
        System.out.println(Arrays.toString(nums)); // [1,3,2]
    }

    public void nextPermutation(int[] nums) {
        if (nums.length == 0 || nums.length == 1) return;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i + 1] > nums[i]) {
                int next = nums[i];
                int index = i;
                for (int j = i; j < nums.length; j++) {
                    if (nums[j] > nums[i]) {
                        if (next == nums[i] || next > nums[j]) {
                            next = nums[j];
                            index = j;
                        }
                    }
                }
                int t = nums[i];
                nums[i] = nums[index];
                nums[index] = t;
                Arrays.sort(nums, i + 1, nums.length);
                return;
            }

        }
        for (int i = 0; i < (nums.length + 1) / 2; i++) {
            int t = nums[i];
            nums[i] = nums[nums.length - 1 - i];
            nums[nums.length - 1 - i] = t;
        }
    }
}
