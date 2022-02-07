package com.leo.leetcode.algorithm.q0000;

public class Q4 {
    /**
     * 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
     * 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
     * 你可以假设 nums1 和 nums2 不会同时为空。
     * 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
     */
    public static void main(String[] args) {
        System.out.println(new Q4().findMedianSortedArrays(new int[]{1, 3}, new int[]{2}));// 2.0
        System.out.println(new Q4().findMedianSortedArrays(new int[]{1, 2}, new int[]{3, 4}));// 2.5
    }

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int limit = nums1.length + nums2.length;
        int count = 0;
        int i = 0;
        int j = 0;
        double ret1 = 0;
        while (true) {
            int value;
            if (i == nums1.length) {
                value = nums2[j++];
            } else if (j == nums2.length) {
                value = nums1[i++];
            } else if (nums1[i] < nums2[j]) {
                value = nums1[i++];
            } else {
                value = nums2[j++];
            }
            count++;
            if (limit % 2 == 0) {
                if (count == limit / 2) {
                    ret1 = value;
                }
                if (count == limit / 2 + 1) {
                    return (ret1 + value) / 2;
                }
            } else {
                if (count == (limit + 1) / 2) {
                    return value;
                }
            }
        }
    }
}
