package com.leo.leetcode.algorithm;

public class Q33 {
    public int search(int[] nums, int target) {
        return s(nums, target, 0, nums.length - 1);
    }

    int s(int[] nums, int target, int start, int end) {
        if (start > end) return -1;
        int i = start + (end - start + 1) / 2;
        if (nums[i] == target) {
            return i;
        }
        int l = s(nums, target, start, i - 1);
        if (l != -1) {
            return l;
        }
        int r = s(nums, target, i + 1, end);
        if (r != -1) {
            return r;
        }

        return -1;
    }
}
