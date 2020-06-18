package com.leo.leetcode.algorithm;

import java.util.Arrays;

public class Q75 {
    public static void main(String[] args) {
        new Q75().TestOJ();
    }

    public void TestOJ() {
        System.out.println(Arrays.toString(sortColors(new int[]{2, 0, 2, 1, 1, 0})));
        System.out.println(Arrays.toString(sortColors(new int[]{2, 0, 1})));
        System.out.println(Arrays.toString(sortColors(new int[]{1, 2, 0})));
        System.out.println(Arrays.toString(sortColors(new int[]{0, 0, 2, 1, 2, 2})));
    }

    public int[] sortColors(int[] nums) {
        int l = 0;
        int r = nums.length - 1;

        for (int i = 0; i <= r; ) {
            int v = nums[i];
            if (v == 0) {
                nums[i] = nums[l];
                nums[l] = v;
                l++;
                i++;
            } else if (v == 2) {
                nums[i] = nums[r];
                nums[r] = v;
                r--;
            } else {
                i++;
            }
        }
        return nums;
    }
}
