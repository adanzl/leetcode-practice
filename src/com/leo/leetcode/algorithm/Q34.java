package com.leo.leetcode.algorithm;

public class Q34 {
    public int[] searchRange(int[] nums, int target) {
        int ret = s(nums, target, 0, nums.length - 1);
        if (ret == -1) return new int[]{-1, -1};
        int l = ret;
        while (l > 0 && nums[l - 1] == target) l--;
        int r = ret;
        while (r < nums.length - 1 && nums[r + 1] == target) r++;
        return new int[]{l, r};
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
