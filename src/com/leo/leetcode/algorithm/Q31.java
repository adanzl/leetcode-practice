package com.leo.leetcode.algorithm;

import java.util.Arrays;

public class Q31 {
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
