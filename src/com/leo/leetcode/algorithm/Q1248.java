package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q1248 {

    public static void main(String[] args) {
        System.out.println(new Q1248().numberOfSubArrays(LCUtil.stringToIntegerArray("[2,2,2,1,2,2,1,2,2,2,1]"), 2)); // 16
    }

    public int numberOfSubArrays(int[] nums, int k) {
        int out = 0, cOdd = 0;
        int[] arr = new int[nums.length + 1];
        arr[0] = 1;
        for (int num : nums) {
            cOdd += (num & 1);
            arr[cOdd]++;
            if (cOdd >= k) out += arr[cOdd - k];
        }
        return out;
    }
}
