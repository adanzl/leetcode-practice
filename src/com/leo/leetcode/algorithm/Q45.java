package com.leo.leetcode.algorithm;

public class Q45 {
    public static void main(String[] args) {
        System.out.println(new Q45().jump(new int[]{1, 1, 1, 1})); // 3
        System.out.println(new Q45().jump(new int[]{7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3})); // 2
        System.out.println(new Q45().jump(new int[]{2, 3, 1, 1, 4})); // 2
        System.out.println(new Q45().jump(new int[]{1, 2, 3})); // 2
        System.out.println(new Q45().jump(new int[]{2, 1})); // 1
        System.out.println(new Q45().jump(new int[]{1, 3})); // 1
        System.out.println(new Q45().jump(new int[]{1})); // 0
    }

    public int jump(int[] nums) {
        int out = 0, limit = 0, flag = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            limit = Math.max(i + nums[i], limit);
            if (limit >= nums.length - 1) return out + 1;
            if (i == flag) {
                flag = limit;
                out++;
            }
        }
        return out;
    }
}
