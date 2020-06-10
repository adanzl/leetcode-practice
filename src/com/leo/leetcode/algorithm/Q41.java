package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q41 {

    public static void main(String[] args) {
        System.out.println(new Q41().firstMissingPositive(LCUtil.stringToIntegerArray("[3,4,-1,1]"))); // 2
        System.out.println(new Q41().firstMissingPositive(LCUtil.stringToIntegerArray("[2,1]"))); // 3
        System.out.println(new Q41().firstMissingPositive(LCUtil.stringToIntegerArray("[1,1]"))); // 2
        System.out.println(new Q41().firstMissingPositive(LCUtil.stringToIntegerArray("[1]"))); // 2
        System.out.println(new Q41().firstMissingPositive(LCUtil.stringToIntegerArray("[1,2,0]"))); // 3
        System.out.println(new Q41().firstMissingPositive(LCUtil.stringToIntegerArray("[7,8,9,11,12]"))); // 1
    }

    public int firstMissingPositive(int[] nums) {
        if (nums.length == 0) return 1;
        if (nums.length == 1 && nums[0] == 1) return 2;
        for (int i = 0; i < nums.length; ) {
            int v = nums[i] - 1;
            if (v < 0 || v > nums.length - 1 || nums[i] == nums[v]) {
                i++;
                continue;
            }
            swap(nums, i, v);
        }
        int index = 0;
        for (; index < nums.length; index++) {
            if (nums[index] != index + 1) return index + 1;
        }
        if (index == nums.length) return index + 1;
        return 1;
    }

    void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
}
