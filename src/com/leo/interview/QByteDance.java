package com.leo.interview;

public class QByteDance {

    public static void main(String[] args) {
        System.out.println(new QByteDance().search(new int[]{1, 3, 1, 1}, 3)); // 1
        System.out.println(new QByteDance().search(new int[]{1, 3, 5}, 5)); // 2
        System.out.println(new QByteDance().search(new int[]{4, 5, 6, 7, 0, 1, 2}, 0)); // 4
    }

    public int search(int[] nums, int target) {
        return s(nums, 0, nums.length, target);
    }

    int s(int[] nums, int start, int end, int target) {
        if (start >= end) return -1;
        int mid = (end + start) >> 1;
        if (nums[mid] == target) return mid;
        if ((nums[start] > target) ^ (nums[start] > nums[mid]) ^ (target > nums[mid]))
            return s(nums, mid + 1, end, target);
        return s(nums, start, end - 1, target);
    }
}
