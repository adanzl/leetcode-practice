package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class Q283 {

    public static void main(String[] args) {
        new Q283().TestOJ();
    }

    public void TestOJ() {
        int[] nums = LCUtil.stringToIntegerArray("[0,1,0,3,12]");
        moveZeroes(nums);
        System.out.println(Arrays.toString(nums)); // [1,3,12,0,0]
    }

    public void moveZeroes(int[] nums) {
        int p = 0;
        for (int i = 0; i < nums.length; i++) {
            nums[p] = nums[i];
            if (nums[i] != 0) {
                p++;
            }
        }
        for (int i = p; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
