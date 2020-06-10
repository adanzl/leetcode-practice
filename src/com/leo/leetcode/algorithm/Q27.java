package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q27 {
    public static void main(String[] args) {
        new Q27().TestOJ();
    }

    public void TestOJ() {
        System.out.println(removeElement(LCUtil.stringToIntegerArray("[3,2,2,3]"), 3)); // 2
        System.out.println(removeElement(LCUtil.stringToIntegerArray("[0,1,2,2,3,0,4,2]"), 2)); // 5
    }

    public int removeElement(int[] nums, int val) {
        int count = 0;
        for (int i = 0; i < nums.length - count; ) {
            if (nums[i] == val) {
                if (count < nums.length) {
                    nums[i] = nums[nums.length - 1 - count];
                }
                count++;
            } else {
                i++;
            }
        }

        return nums.length - count;
    }

}
