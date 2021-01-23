package com.leo.leetcode.algorithm.q0100;

import java.util.Arrays;

/**
 * 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
 * 进阶：
 * 1、尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
 * 2、你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
 * <p>
 * 链接：https://leetcode-cn.com/problems/rotate-array
 */
public class Q189 {

    public static void main(String[] args) {
        int[] nums;
        nums = new int[]{1};
        new Q189().rotate(nums, 2);
        System.out.println(Arrays.toString(nums)); // [1]
        nums = new int[]{-1, -100, 3, 99};
        new Q189().rotate(nums, 2);
        System.out.println(Arrays.toString(nums)); // [3,99,-1,-100]
        nums = new int[]{1, 2, 3, 4, 5, 6, 7};
        new Q189().rotate(nums, 3);
        System.out.println(Arrays.toString(nums)); // [5,6,7,1,2,3,4]
    }

    public void rotate(int[] nums, int k) {
        k %= nums.length;
        swap(nums, 0, nums.length);
        swap(nums, 0, k);
        swap(nums, k, nums.length);
    }

    void swap(int[] nums, int s, int e) {
        int mid = (e - s) / 2;
        for (int i = 0; i < mid; i++) {
            int v = nums[s + i], i1 = e - 1 - i;
            nums[s + i] = nums[i1];
            nums[i1] = v;
        }
    }
}
