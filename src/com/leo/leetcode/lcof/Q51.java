package com.leo.leetcode.lcof;

import com.leo.utils.LCUtil;

public class Q51 {

    public static void main(String[] args) {
        new Q51().TestOJ();
    }

    public void TestOJ() {
        System.out.println(reversePairs(LCUtil.stringToIntegerArray("[1,3,2,3,1]"))); // 4
        System.out.println(reversePairs(LCUtil.stringToIntegerArray("[]"))); // 0
        System.out.println(reversePairs(LCUtil.stringToIntegerArray("[7,5,6,4]"))); // 5
    }

    public int reversePairs(int[] nums) {
        return mergeSort(nums, 0, nums.length - 1, new int[nums.length]);
    }

    int mergeSort(int[] nums, int l, int r, int[] tmp) {
        if (l >= r) return 0;
        int mid = l + ((r - l) >> 1), out = 0;
        out += mergeSort(nums, l, mid, tmp);
        out += mergeSort(nums, mid + 1, r, tmp);
        out += merge(nums, l, mid, mid + 1, r, tmp);
        return out;
    }

    int merge(int[] nums, int s1, int e1, int s2, int e2, int[] tmp) {
        int p = 0, i = 0, out = 0, s = s1;
        while (s1 <= e1 && s2 <= e2) {
            if (nums[s1] <= nums[s2]) {
                tmp[p++] = nums[s1++];
            } else {
                tmp[p++] = nums[s2++];
                out += e1 - s1 + 1;
            }
        }
        while (s1 <= e1) tmp[p++] = nums[s1++];
        while (s2 <= e2) tmp[p++] = nums[s2++];
        while (i < p) nums[s + i] = tmp[i++];
        return out;
    }
}
