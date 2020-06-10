package com.leo.leetcode.algorithm;

public class Q53 {

    public static void main(String[] args) {
        new Q53().TestOJ();
    }

    public void TestOJ() {
        System.out.println(maxSubArray(new int[]{-2, 1}));
        System.out.println(maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
    }

    public int maxSubArray(int[] nums) {
        int ret = nums[0];
        int[] arr = new int[nums.length];
        arr[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (arr[i - 1] > 0) {
                arr[i] = arr[i - 1] + nums[i];
            } else {
                arr[i] = nums[i];
            }
            ret = Math.max(ret, arr[i]);
        }

        return ret;
    }
}
