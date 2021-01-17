package com.leo.leetcode.algorithm.q0000;

public class Q55 {
    public void TestOJ() {
        System.out.println(canJump1(new int[]{3, 2, 1, 0, 2,4})); // f
//        System.out.println(canJump(new int[]{2, 3, 1, 1, 4})); // t
//        System.out.println(canJump(new int[]{0})); // t
    }

    public boolean canJump1(int[] nums) {
        int lastPos = nums.length - 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i + nums[i] >= lastPos) {
                lastPos = i;
            }
        }
        return lastPos == 0;
    }

    public boolean canJump(int[] nums) {
        return tryJump(nums, 0);
    }

    boolean tryJump(int[] nums, int index) {
        int v = nums[index];
        if (index + v >= nums.length - 1) return true;
        if (v == 0) return false;
        for (int i = v; i > 0; i--) {
            if (tryJump(nums, index + i))
                return true;
        }
        nums[index] = 0;
        return false;
    }
}
