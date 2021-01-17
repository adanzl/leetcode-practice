package com.leo.leetcode.algorithm.q0000;

public class Q26 {
    public int removeDuplicates(int[] nums) {

        if (nums.length <= 1) return nums.length;
        int ret = nums.length;
        int index = 0;
        for (int i = 1; i < nums.length; i++) {
            int v = nums[i];
            if (v == nums[i - 1]) {
                ret--;
            } else {
                nums[++index] = nums[i];
            }
        }

        return ret;
    }
}
