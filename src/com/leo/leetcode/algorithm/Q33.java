package com.leo.leetcode.algorithm;

public class Q33 {

    public static void main(String[] args) {
        System.out.println(new Q33().search(new int[]{4, 5, 6, 7, 0, 1, 2}, 0)); // 4
        System.out.println(new Q33().search(new int[]{4, 5, 6, 7, 0, 1, 2}, 3)); // -1
    }

    public int search(int[] nums, int target) {
        return s(nums, target, 0, nums.length - 1);
    }

    int s(int[] nums, int target, int start, int end) {
        if (start > end) return -1;
        int i = start + (end - start + 1) >> 1;
        if (nums[i] == target) return i;
        int l = s(nums, target, start, i - 1);
        if (l != -1) return l;
        return s(nums, target, i + 1, end);
    }
}
