package com.leo.leetcode.algorithm;

/**
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 * ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
 * 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
 * 你可以假设数组中不存在重复的元素。
 * 你的算法时间复杂度必须是 O(log n) 级别。
 * 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
 */
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
