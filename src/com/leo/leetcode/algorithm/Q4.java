package com.leo.leetcode.algorithm;

public class Q4 {
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
