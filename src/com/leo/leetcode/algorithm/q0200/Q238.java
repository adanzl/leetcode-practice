package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class Q238 {
    public static void main(String[] args) {
        new Q238().TestOJ();
    }

    public void TestOJ() {
        System.out.println(Arrays.toString(productExceptSelf(LCUtil.stringToIntegerArray("[1,2,3,4,5]")))); // [120, 60, 40, 30, 24]
        System.out.println(Arrays.toString(productExceptSelf(LCUtil.stringToIntegerArray("[1,2]")))); // [2,1]
    }

    private int[] productExceptSelf(int[] nums) {
        int[] ret = new int[nums.length];
        int flag = nums[0];
        ret[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            ret[i] = flag;
            flag *= nums[i];
        }
        flag = nums[nums.length - 1];
        for (int i = nums.length - 2; i >= 0; i--) {
            ret[i] *= flag;
            flag *= nums[i];
        }
        return ret;
    }
}
