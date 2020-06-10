package com.leo.leetcode.algorithm;

import org.junit.Test;

public class Q27 {

    @Test
    public void TestOJ() {
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
