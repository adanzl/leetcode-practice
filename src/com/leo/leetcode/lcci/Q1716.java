package com.leo.leetcode.lcci;

public class Q1716 {

    public static void main(String[] args) {
        System.out.println(new Q1716().massage(new int[]{1, 2, 3, 1})); // 4
        System.out.println(new Q1716().massage(new int[]{2, 7, 9, 3, 1})); // 12
        System.out.println(new Q1716().massage(new int[]{2, 1, 4, 5, 3, 1, 1, 3})); // 12
    }

    public int massage(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        int[] mark = new int[nums.length];
        mark[0] = nums[0];
        mark[1] = Math.max(nums[0], nums[1]);
        int out = mark[0];
        for (int i = 2; i < nums.length; i++) {
            mark[i] = Math.max(mark[i - 1], mark[i - 2] + nums[i]);
            out = Math.max(out, mark[i]);
        }
        return out;
    }
}
