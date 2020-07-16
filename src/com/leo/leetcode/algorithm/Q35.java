package com.leo.leetcode.algorithm;

/**
 * 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
 * 你可以假设数组中无重复元素。
 * 链接：https://leetcode-cn.com/problems/search-insert-position/
 */
public class Q35 {
    public static void main(String[] args) {
        System.out.println(new Q35().searchInsert(new int[]{1, 3, 5, 6}, 2)); // 1
        System.out.println(new Q35().searchInsert(new int[]{1, 3, 5, 6}, 5)); // 2
        System.out.println(new Q35().searchInsert(new int[]{1, 3, 5, 6}, 7)); // 4
        System.out.println(new Q35().searchInsert(new int[]{1, 3, 5, 6}, 0)); // 0
    }

    public int searchInsert(int[] nums, int target) {
        int l = 0, r = nums.length;
        if (target < nums[l]) return 0;
        if (target > nums[r - 1]) return r;
        while (l < r) {
            int mid = (r + l) >> 1;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) l = mid + 1;
            else r = mid;
        }
        return l;
    }
}
